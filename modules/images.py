import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Context
from discord import Interaction
from discord import Embed
from lists.interactions import *
from lists.images import *
import requests
import random



class AnimeImage():
    async def trap(ctx):
        await ctx.send(random.choice(Anime.traps))



    async def waifu(category):
        if category == '':
            category = 'waifu'
        try:
            r = requests.get(f'https://api.waifu.pics/sfw/{category}')
            data = r.json()
            url = data['url']
            return (url)
        except:
            return(f'Erro.')

