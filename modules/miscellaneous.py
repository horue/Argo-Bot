import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Context
from discord import Interaction
from discord import Embed
from lists.interactions import *
from lists.images import *
from .utils.recomendations import *


class Misc():
    async def sessão(ctx):
        return('Eu ouvi sessão?')


    async def recomendar(ctx):
        url, title = mandar()
        return(f'**{ctx.author.mention}, minha recomendação pra você é**: {title}\n{url}')

    async def pobre(ctx):
        return('https://imgur.com/S8uJQVm')


    async def multi(ctx):
        return('esse jogo e multi, voces nao tem idea da mídia do ps4 eles pagam pelo jogo que voces jogam sao mais caros e mais evoluídos assim e diferente e voce nunca ira entender pois sao infieis ao console')
