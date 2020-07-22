import random
import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #drzewo
    @commands.command()
    async def wyruchaj_drzewo(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.green()
        )

        embed.set_author(name='Dobrze ci poszło!')
        #embed.add_field(name="Dobrze ci poszło!", value=None, inline=False)
        await ctx.send(embed=embed)
        print('Ktoś ma dziwny fetysz..')

    #pinge
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def pinge(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        await ctx.send('@everyone')
        print('Spingowano wszystkich')

    #abot
    @commands.command()
    async def abot(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.green()
        )
        
        embed.set_author(name='Ale seksiak..')
        embed.set_image(url='https://i.gyazo.com/de1b35f2ae5f7e64f0f606104b4f42c9.png')
        await ctx.send(embed=embed)
        print('Wysłano awatar bota na czyjeś życzenie')


    #fraszka
    @commands.command()
    async def fraszka(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.green()
        )

        embed.set_author(name='Lambert, Lamber, ty chuju..')
        await ctx.send(embed=embed)
        print('Mamy tu poetę..')

    #elfy to geje
    @commands.command()
    async def łucznik(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.green()
        )

        embed.set_author(name='elf leśny gej')
        await ctx.send(embed=embed)
        print('Elf is gay')

    #power level
    @commands.command()
    async def power(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.green()
        )

        embed.add_field(name="Mój skauter mówi, że twój poziom mocy to:", value=random.randint(5,10000), inline=False)
        embed.set_image(url='https://i.gyazo.com/3a9d663007d0a80448ea02fa58817f33.png')

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Example(client))
