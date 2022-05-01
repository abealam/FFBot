import discord
from discord.ext import commands
import os
import random
import TOKEN

client = commands.Bot(command_prefix='!')


@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."
                 ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.sent('loaded')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.sent('unloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(TOKEN)




# import lightbulb
# import hikari
# from datetime import datetime
# import string
# import passing
#
# bot = lightbulb.BotApp(
#     token='ODQ3MTc3NDg2NTU0MzY1OTY0.YK6RhA.UEsm91GBvpaJgrGmlOqqJUo7fUo',
#     default_enabled_guilds=(745374634312204388)
# )
#
#
# @bot.listen(hikari.StartedEvent)
# async def on_started(event):
#     print('bot has started')
#
#
# @bot.command
# @lightbulb.command('ping', 'says pong!')
# @lightbulb.implements(lightbulb.SlashCommand)
# async def ping(ctx):
#     await ctx.respond('pong!')
#
#
# @bot.command
# @lightbulb.command('todo', 'gives a todo list')
# @lightbulb.implements(lightbulb.SlashCommand)
# async def ping(ctx):
#     await ctx.respond('Cancel FP subscription 9/21/2022')
#     now = datetime.now()
#     toDate = datetime(2022, 9, 21, 23, 59, 59)
#     daysLeft = toDate - now
#     await ctx.respond(daysLeft)
#
#
# @bot.command
# @lightbulb.command('qb', 'Access QB data')
# @lightbulb.implements(lightbulb.SlashCommandGroup)
# async def qb_group(ctx, arg):
#     passing.quarterback_stats(arg)
#     await ctx.respond('success')
#
#
# bot.run()



