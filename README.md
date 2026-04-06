# Pickleball Paddle Discord Bot

A Python-based Discord bot that monitors UPA-A and USA Pickleball for new paddle approvals and sends structured updates to a Discord channel.

## Features
- Periodically checks for new paddles (every 1 hour by default).
- Supports **UPA-A** (United Pickleball Association) and **USA Pickleball**.
- Displays paddle image, name, brand, and approval date.
- Uses SQLite to track "seen" paddles and avoid duplicate notifications.

## Requirements
- Python 3.9+
- Discord Bot Token (with Message Send permissions)

## Setup
1. Clone the repository or download the files.
2. Create a folder named `paddle-discord-bot` and place the files inside.
3. Install dependencies:
   ```bash
   pip install discord.py requests beautifulsoup4 python-dotenv apscheduler
   ```
4. Copy `.env.example` to `.env` and fill in your details:
   - `DISCORD_TOKEN`: Your bot's secret token from the [Discord Developer Portal](https://discord.com/developers/applications).
   - `CHANNEL_ID`: The numeric ID of the Discord channel where updates should be posted.

## Files
- `bot.py`: The main entry point. Handles Discord connection and scheduling.
- `scraper.py`: Contains the scraping logic for both sites.
- `database.py`: Manages the SQLite database (`paddles.db`) to track seen paddles.
- `.env`: (You create this) Stores your secret tokens.

## Running the Bot
```bash
python bot.py
```

## How it Works
- The bot scrapes the first page of USA Pickleball and the full UPA-A list.
- It generates a unique key for each paddle based on Brand + Model + Source.
- If a key isn't in `paddles.db`, it sends an embed to Discord and saves the key.
- On the very first run, it will detect all currently listed paddles as "new" (unless you manually populate the DB or the script is modified to skip the first batch).
