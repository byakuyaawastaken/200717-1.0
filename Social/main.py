import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('200717,1.0'))
    print('Social jest gotowy do działania')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print('Pomyślnie załadowano')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print('Pomyślnie odładowano')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzMwMTMyNTM2MzczNjc0MDc3.XwTDBw.bbhWuMN0O_vrgymbgtxgvT6aqt0')
