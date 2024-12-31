import time
import schedule
import asyncio
from telegram import Bot

# Replace with your bot token from BotFather
BOT_TOKEN = "7679618788:AAG-56rgPUv0goOiSY4tYh_C6OEaJkEFJxg"

# List of chat IDs or channel IDs where the message will be sent
CHAT_IDS = [
    "@daily_crypto_minner",  # Replace with your Telegram channel ID or group ID
    "@JOINKARLOTUMHARAFAYDA",  # Add more chat IDs as needed
]

# Initialize the bot
bot = Bot(token=BOT_TOKEN)

async def send_new_year_wish():
    """
    Function to send a New Year greeting message to multiple chats or channels.
    """
    message = """
🎆 **Happy New Year 2025, Amazing Members!** 🎆

As we enter a brand-new year, I want to take a moment to express my heartfelt gratitude for being part of this incredible community. Your presence and support make all the difference!  

✨ May this year bring you:  
- **Opportunities** that elevate your journey,  
- **Happiness** that brightens your days, and  
- **Success** in every endeavor you pursue.  

Together, let’s make 2025 a year of inspiration, growth, and achievements.  

**Thank you for being here, and cheers to a fantastic year ahead!** 🥂  

Warm regards,  
**Jagat Singh**
    """
    
    for chat_id in CHAT_IDS:
        try:
            await bot.send_message(chat_id=chat_id, text=message, parse_mode="Markdown")
            print(f"Message sent to chat ID: {chat_id}")
        except Exception as e:
            print(f"Failed to send message to chat ID: {chat_id}. Error: {e}")

def schedule_task():
    """
    Function to schedule the task to send a New Year wish.
    """
    # This will create an asyncio task without blocking
    asyncio.create_task(send_new_year_wish())

async def main():
    # Schedule the message to be sent at 12:00 AM today
    schedule.every().day.at("00:00").do(schedule_task)
    
    print("Bot is running. Waiting to send the New Year wish at 12:00 AM...")
    
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

# Run the main async function
if __name__ == '__main__':
    asyncio.run(main())
