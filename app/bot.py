# base imports
import os
from dotenv import load_dotenv
import random
import math
import functools
import itertools
import asyncio
import json

# discord imports
import discord
from discord.ext import commands
from discord.utils import get

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

##############################
##### SET COMMAND SYNTAX #####
##############################

bot = commands.Bot('.', description='don\'t say uwu')

####################
##### ADD COGS #####
####################

# maybe put module imports here too

# bot.add_cog(Gamble(bot))

###############################
##### EVENTS FOR TERMINAL #####
###############################

@bot.event
async def on_ready():
    print('Logged in as: \n{0.user.name}\n{0.user.id}'.format(bot))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

###################
##### RUN BOT #####
###################

bot.run(TOKEN)