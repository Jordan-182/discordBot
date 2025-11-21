import discord
import os
from dotenv import load_dotenv
load_dotenv()

print("Lancement du bot")
bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Bot allumé")

@bot.event
async def on_message(message: discord.message):
  if message.author.bot:
    return
  if message.content.lower() == "bonjour":
    channel = message.channel
    author = message.author
    await channel.send('Comment tu vas?')
  if message.content.lower() == "bienvenue":
    welcome_channel = bot.get_channel(1441521236021743808)
    await welcome_channel.send("Bienvenue!")

bot.run(os.getenv('DISCORD_TOKEN'))