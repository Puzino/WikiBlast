# Telegram Bot with Scheduled Wikipedia Pages 🎟️

This is a Telegram bot that automatically sends Wikipedia pages three times a day at scheduled times using `aiogram`, `apscheduler`, and `Wikipedia-API`.

## 🔥 Features

- Sends a random Wikipedia page automatically at **09:00, 13:00, and 18:00 UTC-1**
- Runs without requiring user commands
- Uses `aiogram` for handling Telegram updates
- Uses `apscheduler` for scheduling tasks
- Uses `Wikipedia-API` to fetch Wikipedia content
- Uses `MechanicalSoup` to get a random page from Wikipedia
- Supports **Docker** for easy deployment

---

## 🛠️ Installation

Before running the bot, ensure you have Python 3.8+ installed.

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Puzino/WikiBlast.git
cd WikiBlast
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Create a `.env` file for configuration
Create a `.env` file and add your bot token and chat ID:

```bash
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id
```

### 4️⃣ Create a `database.csv` file for save your pages
```bash
touch database.csv
```

---

## 🚀 Running the bot
```bash
python aiogram_run.py
```

---

## 🐙 Running with Docker

### 1️⃣ Build the Docker image:
```bash
docker build -t telegram-bot .
```

### 2️⃣ Run the container:
```bash
docker run -d --env-file .env --name telegram-bot telegram-bot
```

### 3️⃣ Stop the container:
```bash
docker stop telegram-bot
```

### 4️⃣ Remove the container:
```bash
docker rm telegram-bot
```

---

## 🛆 Running with Docker Compose

### 1️⃣ Build and start the container:
```bash
docker-compose up -d --build
```

### 2️⃣ Check logs:
```bash
docker-compose logs -f
```

### 3️⃣ Restart the bot after changes:
```bash
docker-compose up --build -d
```

### 4️⃣ Stop and remove the container:
```bash
docker-compose down
```

---

## ⚙️ Technologies Used

- **aiogram** – Asynchronous Python framework for Telegram API
- **apscheduler** – Task scheduler for running messages at scheduled times
- **asyncio** – Python’s built-in asynchronous framework for handling tasks
- **Wikipedia-API** – Python package for retrieving Wikipedia pages
- **MechanicalSoup** – A Python library for web scraping and automating browser interactions
- **Docker** – Containerization for easy deployment
- **Docker Compose** – Managing multiple services in a single configuration

---

## 🐝 License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it.

