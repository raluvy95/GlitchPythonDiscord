import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=",")

@bot.event
async def on_ready():
  print("Bot is online!")

@bot.command()
async def test(ctx): 
  return await ctx.send("Yes, I'm running on Glitch.com!")

bot.run(os.getenv("SECRET"))