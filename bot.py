import discord
from discord.ext import commands
from bot_key import bot_key

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready(): # Ready state for bot
    print("Bot is ready")

client.run(bot_key)