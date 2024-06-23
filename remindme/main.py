import discord

intents = discord.Intents.default()
intents.typing = False
intents.presences = False


client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    return
