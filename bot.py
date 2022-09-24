import discord, os, sys
from discord.ext import commands
import random
from bot_token import token, myid
from receiving import receiving_dict, beautifulWR
from passing import passing_dict, beautifulQB
from rushing import rushing_dict, beautifulRB

description = '''A bot to display fantasy football data'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


def restart_bot():
    os.execv(sys.executable, ['python'] + sys.argv)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('Bot is ONLINE.')


@bot.command()
async def cool(ctx, name):
    if name == "Khai" or name == "Dave":
        await ctx.send(f'{name} is not cool.')
    else:
        await ctx.send(f'{name} is cool.')


@bot.command(description='To choose a flex')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command(description='To get QB stats')
async def QB(ctx, name, stat=None):
    QB_dict = passing_dict()
    if name in QB_dict:
        player = QB_dict[name]
        if not stat:
            await ctx.send(f'{name}\n{beautifulQB(player)}')
        else:
            if stat in player:
                await ctx.send(stat, player[stat])
            else:
                await ctx.send("No such stat exists.")


@bot.command(description='To get RB stats')
async def RB(ctx, name, stat=None):
    RB_dict = rushing_dict()
    if name in RB_dict:
        player = RB_dict[name]
        if not stat:
            await ctx.send(f'{name}\n{beautifulRB(player)}')
        else:
            if stat in player:
                await ctx.send(stat, player[stat])
            else:
                await ctx.send("No such stat exists.")

@bot.command()
async def WR(ctx, name, stat=None):
    WR_dict = receiving_dict()
    if name in WR_dict:
        player = WR_dict[name]
        if not stat:
            await ctx.send(f'{name}\n{beautifulWR(player)}')
        else:
            if stat in player:
                await ctx.send(stat, player[stat])
            else:
                await ctx.send("No such stat exists.")


@bot.command(name='restart')
async def restart(ctx):
    id = str(ctx.author.id)
    if id == myid():
        await ctx.send("Refreshing stats...")
        restart_bot()
    else:
        await ctx.send("You are not an authorized user..")

bot.run(token())
