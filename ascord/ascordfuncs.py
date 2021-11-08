import os
    
def ncord(bot_name, c_prefix, token):
    script = f'''
# embed script
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = f"{c_prefix}")
# Generated using Astro Cord
@bot.event
async def on_ready():
    print("bot is online")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hey there!")

@bot.command()
async def embed(ctx):
    sample_embed = discord.Embed(
        title = "This is a sample embed",
        colour = discord.Colour.red()
    )
    sample_embed.add_field(name = 'This is a sample field', value='This is a field value', inline=False)
    sample_embed.set_image(url=ctx.author.avatar_url)
    sample_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    sample_embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
    sample_embed.set_footer(text="This is a footer")
    await ctx.send(embed = sample_embed)

bot.run(f"{token}")
        '''
    botfile = open(f"{bot_name}.py", "w")
    botfile.write(script)
    print("Generated!")

def as_cogs(bot_name, c_prefix, token):
    os.makedirs(f"{bot_name}/cogs")
    botfile = open(f"{bot_name}/cogs/start.py", "w")
    botfile_main = open(f"{bot_name}/main.py", "w")
    botfile.write(f"""
import discord
from discord.ext import commands
from discord import DMChannel
import random
from datetime import datetime
from discord import Intents

class Start(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')
        await self.client.change_presence(status = discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='Developed by Astro Inc. || m!help'))
        
    @commands.command()
    async def test(self, ctx):
        await ctx.send('Hello there')

    

def setup(client):
    client.add_cog(Start(client))

    
    
    """)
    botfile_main.write(f"""
import discord
from discord.ext import commands
import os
from discord.utils import get
import praw
from discord.ext.commands import Bot
import platform
import asyncio
from discord import Intents


intents = Intents.all()

client = commands.Bot(command_prefix='{c_prefix}')""" + """\n
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'```Loaded {extension} extension```')

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'```Unloaded `{extension}` extension```')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


""" + f"""
client.run(f'{token}')
""")
    print("Generated!!")



