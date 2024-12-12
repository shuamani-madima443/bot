import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up bot with command prefix '!'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    """Responds with a friendly hello message"""
    await ctx.send(f'Hello {ctx.author.name}! 👋')

@bot.command(name='ping')
async def ping(ctx):
    """Check the bot's latency"""
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! Latency: {latency}ms')

@bot.command(name='movie')
async def movie(ctx):
    """Sends the Severence episode video file"""
    try:
        with open('severence_s1_e1.mp4', 'rb') as f:
            file = discord.File(f)
            await ctx.send(file=file)
    except FileNotFoundError:
        await ctx.send("Sorry, the movie file could not be found.")
    except Exception as e:
        await ctx.send(f"An error occurred while sending the file: {str(e)}")

# Run the bot
if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_TOKEN'))
