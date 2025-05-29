# ⚽ Football Match Scraper

A Python script that scrapes daily football matches from [YallaKora](https://www.yallakora.com/) and automatically sends the match details to your email inbox.

---

## 📌 Features

- Scrapes today’s football matches using `requests` and `BeautifulSoup`
- Automatically sends match details via email using `smtplib`
- Extracts:
  - Championship name
  - Team names
  - Final score
  - Match time
- Uses `.env` for secure email credentials

---

## 💻 Tech Stack

- Python 3
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- Requests
- smtplib (standard Python library)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 🖼️ Example Output (Email Body)

