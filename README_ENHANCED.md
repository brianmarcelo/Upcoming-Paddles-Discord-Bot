# 🏓 Pickleball Paddle Discord Bot

A Python-based Discord bot that automatically monitors UPA-A and USA Pickleball for new paddle approvals and posts real-time updates to your Discord server.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Discord.py](https://img.shields.io/badge/discord.py-2.3.2-blue.svg)](https://discordpy.readthedocs.io/)

## ✨ Features

- 🔄 **Automatic Monitoring**: Checks for new approved paddles every hour
- 🎨 **Rich Embeds**: Beautiful Discord messages with paddle images and details
- 🔗 **Multiple Sources**: Monitors both UPA-A and USA Pickleball official lists
- 💾 **Smart Deduplication**: SQLite database prevents duplicate notifications
- ⚡ **Instant Alerts**: Posts new approvals to Discord in real-time
- 🚀 **Deploy Anywhere**: Works locally, Heroku, DigitalOcean, or your own server
- 📝 **Easy Setup**: Comprehensive guides and templates included

## 📋 Requirements

- Python 3.9 or higher
- Discord Bot Token (free from [Discord Developer Portal](https://discord.com/developers/applications))
- Discord Server with permissions to add bots

## 🚀 Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/YOUR_USERNAME/paddle-discord-bot.git
cd paddle-discord-bot
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure
```bash
cp .env.example .env
# Edit .env with your Discord token and channel ID
```

### 3. Run
```bash
python bot.py
```

## 📖 Documentation

- **[DISCORD_BOT_SETUP.md](DISCORD_BOT_SETUP.md)** — Complete step-by-step setup guide
  - Creating Discord bot credentials
  - Configuring permissions
  - Local testing
  - Cloud deployment options

- **[QUICK_CHECKLIST.md](QUICK_CHECKLIST.md)** — Quick reference checklist
  - Setup verification steps
  - Troubleshooting guide
  - Customization ideas

- **[CONTRIBUTING.md](CONTRIBUTING.md)** — Contribution guidelines
  - How to add features
  - Code style guidelines
  - Pull request process

## 🔧 Configuration

### Environment Variables (`.env`)

```env
DISCORD_TOKEN=your_bot_token_here
CHANNEL_ID=your_channel_id_here
```

See `.env.example` for all available options.

## 📁 Project Structure

```
paddle-discord-bot/
├── bot.py                      # Main bot logic & Discord integration
├── scraper.py                  # Web scraping for paddle approvals
├── database.py                 # SQLite database management
├── requirements.txt            # Python dependencies
├── .env.example                # Configuration template
├── .gitignore                  # Git ignore rules
├── Procfile                    # Heroku deployment config
├── runtime.txt                 # Python version for Heroku
├── LICENSE                     # MIT License
├── DISCORD_BOT_SETUP.md        # Detailed setup guide
├── QUICK_CHECKLIST.md          # Quick reference
└── CONTRIBUTING.md             # Contribution guidelines
```

## 📤 Deployment Options

### Heroku (Easiest - Free tier available)
```bash
heroku create your-app-name
heroku config:set DISCORD_TOKEN=your_token
heroku config:set CHANNEL_ID=your_channel_id
git push heroku main
```

See [DISCORD_BOT_SETUP.md](DISCORD_BOT_SETUP.md#step-6-deploy-to-a-server-optional) for detailed deployment guides.

### Docker
```bash
docker build -t paddle-bot .
docker run -e DISCORD_TOKEN=token -e CHANNEL_ID=id paddle-bot
```

### Your Own Server
See [DISCORD_BOT_SETUP.md](DISCORD_BOT_SETUP.md) for systemd/supervisor setup.

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Bot offline | Check `DISCORD_TOKEN` in `.env` and bot authorization |
| No messages in Discord | Verify bot has "Send Messages" permission |
| Module not found | Run `pip install -r requirements.txt` |
| Scraper returns nothing | Check if website structure changed, run `python scraper.py` to debug |

See [QUICK_CHECKLIST.md](QUICK_CHECKLIST.md#troubleshooting) for more solutions.

## 🎯 How It Works

1. **Bot starts** → Initializes Discord connection and SQLite database
2. **Hourly check** → Scrapes UPA-A and USA Pickleball official lists
3. **Compare** → Checks if paddle is in database (seen before?)
4. **Alert** → If new, posts rich embed to Discord and saves to database
5. **Repeat** → Checks again in 1 hour

### Data Flow
```
UPA-A Website ──┐
                ├─→ Scraper ──→ Database Check ──→ Discord Embed ──→ Your Channel
USA Pickleball ─┘
```

## 🔄 Monitoring Multiple Lists

Currently monitors:
- ✅ **UPA-A** (United Pickleball Association): Full list
- ✅ **USA Pickleball**: First 2 pages (most recent)

Want to add more sources? See [CONTRIBUTING.md](CONTRIBUTING.md) for instructions.

## 🛠️ Customization

### Change Check Frequency
Edit `bot.py`, line with `scheduler.add_job()`:
```python
scheduler.add_job(check_for_updates, 'interval', hours=2)  # Check every 2 hours
```

### Customize Embed Colors
In `send_paddle_update()` function:
```python
color=0xFF5733  # Change to your favorite hex color
```

### Add More Data Fields
In `send_paddle_update()`:
```python
embed.add_field(name="Custom Field", value="Your Data", inline=False)
```

## 📊 Database

The bot uses SQLite (`paddles.db`) to track seen paddles. This prevents:
- Duplicate messages for same paddle
- Accidental reprocessing after restart
- False alerts from unchanged data

To reset: `rm paddles.db` and restart the bot.

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Ideas
- Add support for additional paddle organizations
- Improve scraper robustness
- Enhanced embed formatting
- Better error handling
- Performance optimizations

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Credits

- Built with [discord.py](https://discordpy.readthedocs.io/)
- Web scraping with [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- Scheduling with [APScheduler](https://apscheduler.readthedocs.io/)

## 📞 Support

- **Found a bug?** [Open an issue](https://github.com/YOUR_USERNAME/paddle-discord-bot/issues)
- **Have a question?** [Start a discussion](https://github.com/YOUR_USERNAME/paddle-discord-bot/discussions)
- **Want to help?** See [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Happy paddle monitoring! 🏓** Let us know what you think and happy pickling! 🥒

---

*Made with ❤️ for the pickleball community*
