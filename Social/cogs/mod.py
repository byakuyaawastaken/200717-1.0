import random
import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #clear
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=50):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(
            colour = discord.Colour.green()
        )

        embed.set_author(name='Pomyślnie wyczyszczono!')
        #embed.add_field(name="Pomyślnie wyczyszczono")
        await ctx.send(embed=embed)
        print('Wyczyszczono wiadomości na czacie')

    #pomoc
    @commands.command()
    async def pomoc(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.green()
        )

        embed.set_image(url ='https://i.gyazo.com/472107f061506f9ec4baa40ca1883b51.png')
        await ctx.send(embed=embed)
        print('Użyto komendy pomoc')

    #kick
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        print('Wykopano osobę z serwera')

    #ban
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        print('Zbanowano osobę')

def setup(client):
    client.add_cog(Example(client))
