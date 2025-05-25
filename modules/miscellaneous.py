import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Context
from discord import Interaction
from discord import Embed
from lists.interactions import *
from lists.images import *
from utils.recomendations import *
import random
import requests


class Misc():
    async def sessão(ctx):
        await ctx.send('Eu ouvi sessão?')


    async def recomendar(ctx):
        url, title = mandar()
        await ctx.send(f'**{ctx.author.mention}, minha recomendação pra você é**: {title}\n{url}')


    async def trap(ctx):
        await ctx.send(random.choice(Anime.traps))



    async def pobre(ctx):
        await ctx.send ('https://imgur.com/S8uJQVm')


    async def multi(ctx):
        await ctx.send('esse jogo e multi, voces nao tem idea da mídia do ps4 eles pagam pelo jogo que voces jogam sao mais caros e mais evoluídos assim e diferente e voce nunca ira entender pois sao infieis ao console')
