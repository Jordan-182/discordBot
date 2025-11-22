import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

print("Lancement du bot")
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Bot allumé")
  # Synchroniser les commandes
  try:
    synced = await bot.tree.sync()
    print(f"Commandes slash synchronisées : {len(synced)}")
  except Exception as e:
    print(e)

@bot.event
async def on_message(message: discord.message):
  # Empêcher le bot de s'activer lui-même
  if message.author.bot:
    return
  if message.content.lower() == "bonjour":
    channel = message.channel
    author = message.author
    await channel.send('Comment tu vas?')
  if message.content.lower() == "bienvenue":
    welcome_channel = bot.get_channel(1441521236021743808)
    await welcome_channel.send("Bienvenue!")

@bot.tree.command(name="test", description="Tester les embed")
async def test(interaction: discord.Interaction):
  embed = discord.Embed(
    title="Test title",
    description="Description de l'embed",
    color=discord.Color.blue()
  )
  embed.add_field(name="Web", value="Apprendre le développement web", inline=False)
  embed.set_footer(text="Pied de page")
  await interaction.response.send_message(embed=embed)

@bot.tree.command(name="warnguy", description="Alerter une personne")
async def warnguy(interaction: discord.Interaction, member: discord.Member):
  await interaction.response.send_message("Alerte envoyée")
  await member.send("Tu as reçu une alerte")

@bot.tree.command(name="banguy", description="Bannir une personne")
async def banguy(interaction: discord.Interaction, member: discord.Member):
  await interaction.response.send_message("Ban envoyé")
  await member.ban(reason="Tu n'es pas abonné")
  await member.send("Tu as été banni")

@bot.tree.command(name="portfolio", description="Afficher mon portfolio")
async def portfolio(interaction: discord.Interaction):
  await interaction.response.send_message("Mon portfolio : https://jordanpieton.fr")

bot.run(os.getenv('DISCORD_TOKEN'))