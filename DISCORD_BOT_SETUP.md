# Pickleball Paddle Discord Bot - Complete Setup Guide

This guide walks you through setting up your Discord bot step-by-step.

---

## Step 1: Create a Discord Application & Bot

### 1.1 Create an Application
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"** (top right)
3. Give it a name: `Paddle Bot` (or your preference)
4. Accept the terms and click **"Create"**

### 1.2 Create a Bot User
1. Go to the **"Bot"** tab on the left sidebar
2. Click **"Add Bot"**
3. Under the bot's username, click **"Reset Token"** to generate your bot token
4. **Copy and save this token securely** — you'll need it for `.env`
   - ⚠️ Never share this token or commit it to GitHub

### 1.3 Set Bot Permissions
1. Still in the **"Bot"** tab, scroll to **"Privileged Gateway Intents"**
2. Toggle **"Message Content Intent"** to ON (needed to read messages)
3. Scroll down to **"TOKEN"** and copy it (if you haven't already)

### 1.4 Set Bot Permissions for Your Server
1. Go to the **"OAuth2"** tab on the left
2. Click **"URL Generator"**
3. Under **"Scopes"**, select:
   - `bot`
4. Under **"Permissions"**, select:
   - `Send Messages`
   - `Embed Links` (for rich embeds)
   - `Read Message History`
5. Copy the generated URL and open it in your browser
6. Select the Discord server where you want the bot to operate
7. Click **"Authorize"**

---

## Step 2: Prepare Your Local Environment

### 2.1 Create Project Directory
```bash
mkdir paddle-discord-bot
cd paddle-discord-bot
```

### 2.2 Copy Your Files
Copy these files into your project folder:
- `bot.py`
- `scraper.py`
- `database.py`
- `README.md`

### 2.3 Create Virtual Environment (Recommended)
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 2.4 Install Dependencies
```bash
pip install discord.py requests beautifulsoup4 python-dotenv apscheduler
```

**What each does:**
- `discord.py` — Discord bot framework
- `requests` — HTTP library for web scraping
- `beautifulsoup4` — HTML parsing for scraping
- `python-dotenv` — Load environment variables from `.env`
- `apscheduler` — Scheduled tasks (hourly paddle checks)

---

## Step 3: Get Your Discord Channel ID

### 3.1 Enable Developer Mode
1. Open Discord and go to **User Settings** (gear icon)
2. Go to **"Advanced"** tab
3. Toggle **"Developer Mode"** ON

### 3.2 Get Channel ID
1. Right-click on the channel where you want paddle updates posted
2. Click **"Copy Channel ID"**
3. Save this ID — you'll need it for `.env`

---

## Step 4: Create `.env` File

Create a file named `.env` in your project directory with:

```env
DISCORD_TOKEN=your_bot_token_here
CHANNEL_ID=your_channel_id_here
```

**Example:**
```env
DISCORD_TOKEN=MTk4NjIyNDgzNDU4MTI4ODk2.Clwa7A.l5PVzJnOU78Xe3CM9vTo-_UZ
CHANNEL_ID=987654321098765432
```

⚠️ **Important:** Add `.env` to `.gitignore` if using Git!
```bash
echo ".env" >> .gitignore
```

---

## Step 5: Test the Bot Locally

### 5.1 Run the Bot
```bash
python bot.py
```

You should see output like:
```
INFO:paddle-bot:Logged in as Paddle Bot (ID: 1234567890)
INFO:paddle-bot:Starting paddle check...
INFO:paddle-bot:Found X paddles from UPA-A.
INFO:paddle-bot:Found Y paddles from USA Pickleball.
```

### 5.2 Verify in Discord
Check your Discord channel—you should see paddle announcements appearing (or none if the list hasn't been updated recently).

### 5.3 Troubleshooting
- **"No CHANNEL_ID set"**: Check your `.env` file and restart the bot
- **"Could not find channel"**: Verify the Channel ID is correct and the bot has access
- **No paddles appearing**: The bot will only announce *new* paddles it hasn't seen before
  - On first run, it saves all current paddles to `paddles.db`
  - Future updates will be announced

---

## Step 6: Deploy to a Server (Optional)

For 24/7 uptime, deploy to a cloud service:

### Option A: Heroku (Easiest, Free Tier Available)
1. Sign up at [heroku.com](https://heroku.com)
2. Create a new app
3. Add these environment variables in **Settings → Config Vars**:
   - `DISCORD_TOKEN`
   - `CHANNEL_ID`
4. Connect your GitHub repo or use the Heroku CLI
5. Deploy!

### Option B: DigitalOcean / AWS / Linode
1. Create a droplet/instance
2. SSH into it
3. Clone your repo
4. Set up a Python environment (same as Step 2)
5. Use `systemd` or `screen` to keep the bot running
6. Optionally, set up a reverse proxy with nginx

### Option C: PythonAnywhere
1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload your files
3. Set up a web app (or scheduled task)
4. Configure environment variables

### Option D: Your Own Server/Raspberry Pi
1. SSH into your server
2. Follow Step 2 to set up the environment
3. Use a process manager like `supervisor` or `systemd` to keep it running
4. Ensure your server has internet access and won't auto-shutdown

---

## Step 7: Monitor & Maintain

### Check the Bot is Running
```bash
# If running locally in a terminal, you'll see logs
# If deployed, check your platform's logs dashboard
```

### Add to Discord Server Permanently
1. Go back to OAuth2 → URL Generator (Step 1.4)
2. Bookmark or save the authorization link
3. You can re-use it to add the bot to other servers

### Database Management
The bot stores seen paddles in `paddles.db` (SQLite). To reset:
```bash
rm paddles.db
python bot.py  # Will recreate on startup
```

---

## Common Issues & Fixes

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'discord'` | Run `pip install discord.py` |
| Bot offline / not responding | Check bot token is correct in `.env` |
| Bot doesn't post messages | Verify bot has "Send Messages" permission in the channel |
| `CHANNEL_ID not set` | Ensure `.env` exists and has `CHANNEL_ID=...` |
| Scraper returns no paddles | Websites may have changed—check `scraper.py` selectors |
| Duplicate messages | Delete `paddles.db` to start fresh |

---

## Next Steps

1. **Customize Messages**: Edit the `send_paddle_update()` function in `bot.py` to change embed colors, text, etc.
2. **Adjust Check Frequency**: Change `hours=1` in `bot.py` to check more/less often
3. **Add More Sources**: Modify `scraper.py` to monitor additional paddle approval sites
4. **Set Up Alerts**: Use webhook URLs in Discord for advanced notifications

---

## File Structure (After Setup)
```
paddle-discord-bot/
├── bot.py                 # Main bot logic
├── scraper.py             # Web scraping functions
├── database.py            # SQLite database management
├── README.md              # Original documentation
├── .env                   # ⚠️ SECRET - Never commit
├── .gitignore             # (add .env here)
├── paddles.db             # SQLite database (auto-created)
└── venv/                  # Virtual environment
```

---

Good luck! 🚀 Let me know if you hit any snags.
