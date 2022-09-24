import requests
import pandas as pd
from bs4 import BeautifulSoup


def rushing_dict():
    link = 'https://www.pro-football-reference.com/years/2022/rushing.htm'

    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')
    table = soup.find('table', class_="per_match_toggle")
    rows = table.find_all('tr')

    playerDic = {}
    for tr in rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        if row:
            name = row[0]
            team = row[1]
            attempts = row[6]
            yards = row[7]
            TDs = row[8]
            YPA = row[11]
            YPG = row[12]
            Fumbles = row[13]

            for i in range(len(name)-1, 0, -1):
                if name[i] == '*' or name[i] == '+':
                    name = name[:-1]

            playerDic[name.replace(" ", "")] = \
                {
                    'team': team,
                    'attempts': attempts,
                    'yards': yards,
                    'TDs': TDs,
                    'YPA': YPA,
                    'YPG': YPG,
                    'fumbles': Fumbles,
               }

    return playerDic


def beautifulRB(player):
    if player:
        string = "attempts: " + player['attempts'] + ", yards: " + player['yards'] + ", TDs: " + player['TDs'] \
        + ", fumbles: " + player['fumbles']
        return string
