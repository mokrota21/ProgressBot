from progress_bot import ProgressBot
import discord

TOKEN = 'MTIxNDU2MjA1MDYzODg4MDgyMQ.GefjxT.6L0mzkNMCkVqE3gvs2g77iZkXWN-IJfKLHBL1w'
client = discord.Client(intents=discord.Intents.all())
progress_bot = ProgressBot(TOKEN=TOKEN, client=client, save_threshold=1)
progress_bot.run_bot()