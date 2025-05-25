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



class Animes():
    async def trap(ctx):
        await ctx.send(random.choice(Anime.traps))
