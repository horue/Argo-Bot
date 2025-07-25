from discord.ext import commands
from discord import app_commands
from discord.ext.commands import Context
from discord import Interaction
from lists.character_generator import *
import random


class CharacterCreator():
    @staticmethod
    async def modernCharacter(ctx):
        idade = random.randint(14,60)
        jobb = random.choice(Modern.menos25) if idade <= 25 else random.choice(Modern.mais26)
        tipos = random.choice(sangue) + random.choice(sanguemm)
        persona= random.choice(personalidades)
        return(f'`Nome:{random.choice(nomesh)} {random.choice(sobrenomeh)}\nIdade: {idade}\nTipo Sanguíneo: {tipos}\nOcupação: {jobb}\nPersonalidade: {persona}`')

    @staticmethod
    async def medievalCharacter(ctx):
        idade = random.randint(20,60)
        jobb = random.choice(Medieval.menos25) if idade <= 25 else random.choice(Medieval.mais26)
        tipos = random.choice(sangue) + random.choice(sanguemm)
        persona= random.choice(personalidades)
        return(f'`Nome:{random.choice(nomesh)} {random.choice(sobrenomeh)}\nIdade: {idade}\nTipo Sanguíneo: {tipos}\nOcupação: {jobb}\nPersonalidade: {persona}`')
