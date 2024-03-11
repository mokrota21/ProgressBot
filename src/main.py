from progress_bot import ProgressBot
import discord

with open('token.txt') as f:
    TOKEN = f.read()

client = discord.Client(intents=discord.Intents.all())
progress_bot = ProgressBot(TOKEN=TOKEN, client=client, save_threshold=1)
progress_bot.run_bot()