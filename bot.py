import discord
import os
import asyncio
import logging
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scraper import scrape_upaa, scrape_usap
from database import init_db, is_new_paddle, save_paddle

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID', 0))

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('paddle-bot')

# Initialize Discord Client
intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def check_for_updates():
    if not CHANNEL_ID:
        logger.warning("No CHANNEL_ID set in .env")
        return
        
    channel = client.get_channel(CHANNEL_ID)
    if not channel:
        logger.warning(f"Could not find channel with ID {CHANNEL_ID}")
        return
        
    logger.info("Starting paddle check...")
    
    # 1. Scrape UPA-A
    upaa_paddles = scrape_upaa()
    for paddle in upaa_paddles:
        if is_new_paddle(paddle['key']):
            logger.info(f"New UPAA paddle found: {paddle['brand']} {paddle['model']}")
            await send_paddle_update(channel, paddle)
            save_paddle(paddle)
            
    # 2. Scrape USAP (first 2 pages should be enough for regular checks)
    usap_paddles = scrape_usap(pages=2)
    for paddle in usap_paddles:
        if is_new_paddle(paddle['key']):
            logger.info(f"New USAP paddle found: {paddle['brand']} {paddle['model']}")
            await send_paddle_update(channel, paddle)
            save_paddle(paddle)

async def send_paddle_update(channel, paddle):
    embed = discord.Embed(
        title=f"New Approved Paddle: {paddle['brand']} {paddle['model']}",
        description=f"**Source:** {paddle['source']}",
        color=0x00ff00 if paddle['source'] == 'UPA-A' else 0x0000ff
    )
    embed.add_field(name="Model", value=paddle['model'], inline=False)
    embed.add_field(name="Brand", value=paddle['brand'], inline=False)
    embed.add_field(name="Added to List", value=paddle['date_added'], inline=False)
    
    if paddle['image_url']:
        embed.set_image(url=paddle['image_url'])
        
    embed.set_footer(text="Pickleball Paddle Bot Monitor")
    await channel.send(embed=embed)

@client.event
async def on_ready():
    logger.info(f'Logged in as {client.user} (ID: {client.user.id})')
    init_db() # Ensure DB is ready
    
    # Start the scheduler
    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_for_updates, 'interval', hours=1) # Run every hour
    scheduler.start()
    
    # Run an initial check on start
    await check_for_updates()

if __name__ == "__main__":
    if not DISCORD_TOKEN:
        print("ERROR: DISCORD_TOKEN not found in environment.")
    else:
        client.run(DISCORD_TOKEN)
