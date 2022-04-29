import lightbulb
import hikari
from datetime import datetime

bot = lightbulb.BotApp(
    token='',
    default_enabled_guilds=(745374634312204388)
)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('bot has started')


@bot.command
@lightbulb.command('ping', 'says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('pong!')


@bot.command
@lightbulb.command('todo', 'gives a todo list')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Cancel FP subscription 9/21/2022')
    now = datetime.now()
    toDate = datetime(2022, 9, 21, 23, 59, 59)
    daysLeft = toDate - now
    await ctx.respond(daysLeft)


bot.run()

