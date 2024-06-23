from discord import Intents
from discord.ext import commands

import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_API_TOKEN")

intents: Intents = Intents.default()
# print all the intents

intents.message_content = True


bot: commands.Bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("------")


@bot.command(name="remindme")
async def remindme(ctx):
    print("working")
    await ctx.send("working")


bot.run(TOKEN)
