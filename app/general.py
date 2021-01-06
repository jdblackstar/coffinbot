import discord
from discord.ext import commands
from discord.utils import get

import random

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command(name='choose')
    async def choose(self, ctx: commands.Context, *choices: str):
        '''
        Chooses between any number of inputs.

        Format:
        .choose [option 1] [option 2] [option 3] ...
        '''
        await ctx.send(random.choice(choices))

    @commands.command(name='roll')
    async def roll(self, ctx: commands.Context, num_dice: int, num_sides: int):
        '''
        Rolls a specified number of dice with a specified number of sides.
        '''
        dice = [
            str(random.choice(range(1, num_sides + 1)))
            for _ in range(num_dice)
        ]
        await ctx.send(', '.join(dice))