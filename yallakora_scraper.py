import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import date

# Set up the SMTP connection
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()


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
    
    print(msg)  # Debug: Output message to console
    
    # Send email with proper headers
    connection.sendmail(
        from_addr="fouratmarouen4@gmail.com", 
        to_addrs="fadimarouen76@gmail.com",
        msg=msg.encode('utf-8')  # Encode the message to handle special characters
    )

# Function to scrape match data from the webpage
def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    
    championships = soup.find_all(name="div", class_="matchCard")
    
    # Extract match details
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

# Fetch matches and send them via email
matches = main(page)
send_to_email(matches=matches)

# Close the SMTP connection
connection.close()
