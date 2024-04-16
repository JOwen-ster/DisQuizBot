# Import discord.py
import discord
from discord.ext import commands
from discord import app_commands

# Import os and load_dotenv to load your bot token from the .env file 
from os import getenv
from dotenv import load_dotenv


# Load discord bot token from .env file
load_dotenv()
TOKEN = getenv("DISCORD_TOKEN")

# Set all non privlleged gateway intents for discord bot
intents = discord.Intents.all() # use discord.Intents.default() if you don't need them all
# for example, if you only need the guilds and message_content intents
# https://discordpy.readthedocs.io/en/latest/api.html#discord.Intents
# intents = discord.Intents.default()
# intents.guilds = True
# intents.message_content = True

# Set a bot prefix to listen for commands
# Create a new discord client with the intents to connect it to the discord gateway
BOT_PREFIX = '$'
client = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

# Listener for when the bot has been connected to the gateway and synced slash commands
@client.event
async def on_ready():
    try:
        synced = await client.tree.sync()
        print(F'Synced {len(synced)} tree command(s).')
        print(F'{client.user} is ready.')
    except Exception as e:
        print(F'Could Not Sync Tree: {e}')


client.run(token=TOKEN)