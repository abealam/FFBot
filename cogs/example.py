import discord
from discord.ext import commands


# example cog for reference
class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    # this is how you make an event in a cog
    async def on_ready(self):
        print('Bot is online.')

    @commands.command()
    # this is how you make a command
    async def ping(self, ctx):
        await ctx.send(f'pong!{round(client.latency * 1000)}ms')


def setup(client):
    client.add_cog(Example(client))
