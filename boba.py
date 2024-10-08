import os
from dotenv import load_dotenv, find_dotenv
import disnake
from disnake.ext import commands
bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all(), test_guilds=[898250287221997598])

load_dotenv(find_dotenv())
token = os.getenv("TOKEN")


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")


@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(token)