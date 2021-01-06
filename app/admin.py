import discord
from discord.ext import commands
from discord.utils import get

import random

class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='speak')
    @commands.has_any_role('admin', 'moderator', 'friend')
    async def rand_response(self, ctx: commands.Context):
        '''
        Returns a random response from the list below
        Would like to expand on this and do some NLP maybe
        '''
        responses = [
            'response 1',
            'response 2',
            'response 3',
            'response 4',
            'response 5',
            'response 6',
            'response 7',
            'response 8',
            'response 9',
            'response 10'
        ]

        response = random.choice(responses)
        await ctx.send(response)

    @commands.command(name='choose')
    async def choose(self, ctx: commands.Context, *choices: str):
        await ctx.send(random.choice(choices))

    @commands.command(name='roll')
    async def roll(self, ctx: commands.Context, num_dice: int, num_sides: int):
        '''
        Rolles a num_dice number of dice with num_sides number of sides
        '''
        dice = [
            str(random.choice(range(1, num_sides + 1)))
            for _ in range(num_dice)
        ]
        await ctx.send(', '.join(dice))