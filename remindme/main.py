from discord import Intents
from discord.ext import commands

from remindme.utils.save import save

import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_API_TOKEN")

intents: Intents = Intents.default()
intents.message_content = True


bot: commands.Bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Server started at {datetime.now()}. I'm proud of you.")


@bot.command(name="remindme")
async def remindme(ctx, time: str, *, reminder: str):
    try:
        save(time, reminder)
        await ctx.send("Okay, I will remind you.")
    except Exception as e:
        print(f"An error occurred: {e}")
        await ctx.send("Sorry, I couldn't set your reminder. Please try again later.")


bot.run(TOKEN)
