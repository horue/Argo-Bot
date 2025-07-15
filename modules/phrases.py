import discord
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Context
from discord import Interaction
from discord import Embed
from lists.phrases import *
import random



class Quote():
    async def maha(ctx):
        return(random.choice(mahaa))

    async def qotd(ctx):
        return(random.choice(qotd))

