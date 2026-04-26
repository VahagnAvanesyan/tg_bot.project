# 🤖 Telegram Bot + FastAPI Web Platform

> A web platform that collects user data through a Telegram bot and displays it as profile cards on a website.

---

## ✨ How it works

1. 👤 User finds the bot on Telegram and sends `/start`
2. 💾 Bot saves name, username, avatar and date to the database
3. 🌐 Website displays all user profile cards in real time

---

## 🛠️ Tech Stack

| Part | Technology |
|------|-----------|
| Bot | python-telegram-bot |
| Backend | FastAPI + Uvicorn |
| Database | SQLite + SQLAlchemy |
| Frontend | HTML + CSS + Jinja2 |

---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/VahagnAvanesyan/tg_bot.project.git
cd tg_bot.project
```

### 2. Install dependencies
```bash
py -m pip install -r requirements.txt
```

### 3. Insert your bot token
In `bot.py` replace:
```python
BOT_TOKEN = "YOUR_TOKEN_FROM_BOTFATHER"
```

### 4. Run the bot (first terminal)
```bash
py bot.py
```

### 5. Run the server (second terminal)
```bash
py -m uvicorn main:app --reload
```

### 6. Open your browser
http://127.0.0.1:8000

## 📁 Project Structure
project/
├── bot.py          # Telegram bot
├── main.py         # FastAPI server
├── database.py     # Database connection
├── models.py       # User model
├── requirements.txt
└── templates/
└── index.html  # Frontend

---

## 👨‍💻 Author

**Vahagn Avanesyan** — [GitHub](https://github.com/VahagnAvanesyan)

