import random
import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #active
    commands.command()
    async def dt(self, ctx):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(
            colour = discord.Colour.green()
        )

        embed.set_author(name='dt')
        #embed.add_field(name="Pomyślnie wyczyszczono")
        await ctx.send(embed=embed)
        print('Debug test')
    
        
    

def setup(client):
    client.add_cog(Example(client))
