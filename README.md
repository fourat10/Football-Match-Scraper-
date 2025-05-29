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

Subject: 29/05/2025 Match Results

Championship: Premier League
Liverpool 2 - 1 Chelsea
Time: 18:00

Championship: La Liga
Barcelona 3 - 0 Valencia
Time: 21:00


---

## 📦 Project Structure

football-scraper/
│
├── match_scraper.py # Main script
├── .env # Environment variables (not committed)
├── .gitignore # Ignores .env file
└── README.md # Project documentation

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/football-scraper.git
cd football-scraper

