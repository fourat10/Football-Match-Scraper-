import os
import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import date
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")

# Set up the SMTP connection
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=EMAIL_USER, password=EMAIL_PASS)

# Input the date for which match data is required
datepage = date.today().strftime('%m/%d/%Y')
page = requests.get(url=f"https://www.yallakora.com/match-center/?date={datepage}")

# Function to send match data via email
def send_to_email(matches):
    # Build the email content
    msg = f"Subject: {date.today().strftime('%d/%m/%Y')} Match Results\n\n"
    for match in matches:
        msg += (f"Championship: {match['championship_title']}\n"
                f"{match['teamA']} {match['score']} {match['teamB']}\n"
                f"Time: {match['time']}\n\n")

    print(msg)  # Optional: Debugging output

    # Send the email
    connection.sendmail(
        from_addr=EMAIL_USER,
        to_addrs=EMAIL_TO,
        msg=msg.encode('utf-8')
    )

# Function to scrape match data from the webpage
def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")

    championships = soup.find_all(name="div", class_="matchCard")

    def get_match_info(champs):
        matches_details = []
        for champ in champs:
            champ_title = champ.contents[1].find("h2").text.strip()
            matches = champ.find_all(name="div", class_="liItem")
            for match in matches:
                teamA = match.select_one(".teamA p").text.strip()
                teamB = match.select_one(".teamB p").text.strip()
                scores = match.select(".MResult .score")
                time = match.select_one(".MResult .time").text.strip()
                score = f"{scores[0].text.strip()} - {scores[1].text.strip()}"

                matches_details.append({
                    "championship_title": champ_title,
                    "teamA": teamA,
                    "teamB": teamB,
                    "score": score,
                    "time": time,
                })
        return matches_details

    return get_match_info(championships)

# Fetch and send matches
matches = main(page)
send_to_email(matches=matches)

# Close connection
connection.close()
