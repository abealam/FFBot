import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests


class Passing(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def QB(self, ctx, *, QBname):
        QBdictionary = quarterback_stats(QBname)
        await ctx.send(QBdictionary)


def setup(client):
    client.add_cog(Passing(client))


def quarterback_stats(QB):
    html_text = requests.get('https://www.pro-football-reference.com/years/2021/passing.htm').text
    soup = BeautifulSoup(html_text, 'lxml')
    table = soup.find('tbody')
    players = table.find_all('td')
    allStats = {}

    for i in range(len(players)):
        data = str(players[i].text)

        if i % 30 == 0:
            key = data
            smallList = {}
            allStats[key] = ''
        elif i % 30 == 1:
            smallList['team'] = data
        elif i % 30 == 7:
            smallList['completions'] = data
        elif i % 30 == 8:
            smallList['attempts'] = data
        elif i % 30 == 9:
            smallList['completion%'] = data
        elif i % 30 == 10:
            smallList['yards'] = data
        elif i % 30 == 11:
            smallList['TDs'] = data
        elif i % 30 == 13:
            smallList['ints'] = data
        elif i % 30 == 17:
            smallList['yards per attempt'] = data
        elif i % 30 == 19:
            smallList['yards per completion'] = data
        elif i % 30 == 20:
            smallList['yards per game'] = data
        elif i % 30 == 29:
            allStats[key] = smallList

    try:
        return allStats[QB]
    except:
        return "QB not found"

