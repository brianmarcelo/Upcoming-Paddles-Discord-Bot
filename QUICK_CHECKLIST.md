# Pickleball Paddle Discord Bot - Quick Setup Checklist

## Pre-Launch Checklist

### Discord Setup (5 min)
- [ ] Create Discord Application at https://discord.com/developers/applications
- [ ] Create Bot User in the application
- [ ] Copy bot token and save securely
- [ ] Enable "Message Content Intent" in Privileged Gateway Intents
- [ ] Generate OAuth2 authorization URL with `bot` scope
- [ ] Select permissions: Send Messages, Embed Links, Read Message History
- [ ] Authorize bot to your Discord server
- [ ] Enable Developer Mode in Discord (User Settings → Advanced)
- [ ] Right-click target channel and copy Channel ID

### Local Setup (10 min)
- [ ] Create project folder: `mkdir paddle-discord-bot`
- [ ] Copy bot.py, scraper.py, database.py, README.md to folder
- [ ] Create virtual environment: `python3 -m venv venv`
- [ ] Activate venv: `source venv/bin/activate` (or Windows equivalent)
- [ ] Install dependencies: `pip install discord.py requests beautifulsoup4 python-dotenv apscheduler`
- [ ] Create `.env` file with DISCORD_TOKEN and CHANNEL_ID
- [ ] Create `.gitignore` with `.env` entry

### Launch (2 min)
- [ ] Run: `python bot.py`
- [ ] Check bot appears online in Discord
- [ ] Wait for first paddle check (should happen immediately)
- [ ] Verify messages appear in target channel or check logs

---

## Verification Steps

### Bot is Running
```bash
# You should see output like:
# INFO:paddle-bot:Logged in as Paddle Bot (ID: 1234567890)
# INFO:paddle-bot:Starting paddle check...
```

### Bot Can Post Messages
- Check that your Discord channel shows incoming paddle announcements
- If not, bot may lack "Send Messages" permission (fix in OAuth2 → Permissions)

### Database is Working
- Check for `paddles.db` file in your project folder
- On first run, all current paddles are saved (no messages sent)
- On subsequent runs (after new paddles added), you'll see messages

---

## Quick Deployment Options

### Local Machine
```bash
# Simple, but bot stops when your computer does
python bot.py
```

### Always-On (Best Options)
1. **Heroku** (easiest)
   - Free tier available
   - Add Procfile: `web: python bot.py`

2. **DigitalOcean** ($5/month)
   - More reliable than free services
   - Full control

3. **Your Own Server/Raspberry Pi**
   - Most control, lowest cost long-term
   - Requires port forwarding / always-on machine

---

## Troubleshooting

### Bot doesn't appear online
**Problem:** Token is wrong or bot wasn't authorized  
**Fix:** 
1. Double-check `DISCORD_TOKEN` in `.env`
2. Re-authorize at https://discord.com/developers/applications (OAuth2 → URL Generator)
3. Restart bot

### "Could not find channel with ID"
**Problem:** CHANNEL_ID is wrong or bot lacks access  
**Fix:**
1. Re-copy Channel ID (right-click channel with Developer Mode on)
2. Verify bot is in the server
3. Check bot permissions in server settings

### No paddle messages appearing
**Problem:** Expected behavior on first run; database stores all current paddles  
**Fix:**
1. First run always initializes database without sending messages
2. Wait for new paddles to be added to official lists
3. Or delete `paddles.db` and restart for a fresh run

### "ModuleNotFoundError: No module named 'discord'"
**Problem:** Dependencies not installed  
**Fix:**
```bash
pip install discord.py requests beautifulsoup4 python-dotenv apscheduler
```

### Scraper returns empty results
**Problem:** Website structure changed, selectors no longer work  
**Fix:**
1. Check https://upaa.unitedpickleball.com/approved-paddles/ and https://equipment.usapickleball.org/paddle-list/ to see if HTML structure changed
2. Update CSS selectors in `scraper.py`
3. Test: `python scraper.py`

### Getting rate-limited or blocked by websites
**Problem:** Too many requests too quickly  
**Fix:**
1. Reduce check frequency in `bot.py` (change `hours=1`)
2. Already has 2-second delay between USAP pages (line 72)
3. Consider caching responses

---

## Customization Ideas

### Change Check Frequency
In `bot.py`, find:
```python
scheduler.add_job(check_for_updates, 'interval', hours=1)
```
Change `hours=1` to your preference (e.g., `hours=2`, `minutes=30`, `hours=4`)

### Change Embed Colors
In `bot.py`, in `send_paddle_update()`:
```python
color=0x00ff00 if paddle['source'] == 'UPA-A' else 0x0000ff
```
Use hex color codes (e.g., `0xFF5733` for orange)

### Add More Fields to Embed
In `send_paddle_update()`, add more fields:
```python
embed.add_field(name="Your Field", value=paddle['your_data'], inline=False)
```

### Monitor Additional Sites
1. Add a new scraper function in `scraper.py`
2. Call it from `check_for_updates()` in `bot.py`
3. Generate unique keys to avoid duplicates

---

## File Permissions & Security

⚠️ **Important Security Notes:**
1. **Never share your bot token** — treat it like a password
2. **Never commit `.env` to Git** — add to `.gitignore`
3. **Limit bot permissions** — only grant what's needed
4. **Restrict bot to specific channels** — use Discord permissions

---

## Support Resources

- Discord.py Documentation: https://discordpy.readthedocs.io/
- Discord Developer Portal: https://discord.com/developers/applications
- BeautifulSoup Docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- APScheduler Docs: https://apscheduler.readthedocs.io/

---

## Ready to Go? 🎉

Once you complete the checklist:
1. Your bot will check for new paddles every hour
2. It'll post to Discord automatically
3. No manual updates needed!

Good luck and enjoy your paddle monitoring bot!
