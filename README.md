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
│\n
├── match_scraper.py # Main script<br>
├── .env # Environment variables (not committed)<br>
├── .gitignore # Ignores .env file<br>
└── README.md # Project documentation<br>

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/football-scraper.git
cd football-scraper
```
### 2. Install Dependencies 
```sh
pip install -r requirements.txt
```

If requirements.txt is missing, you can manually install the dependencies:
```sh
pip install requests beautifulsoup4 lxml python-dotenv
```

### 3. Set Up Environment Variables
Create a .env file in the root directory with the following content:
```sh
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
EMAIL_TO=recipient_email@gmail.com
```
🔐 Tip: For Gmail, use an App Password if you have 2-Step Verification enabled.

### 4. Run the Script

```sh
python match_scraper.py
```

