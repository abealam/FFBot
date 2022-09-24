import requests
import pandas as pd
from bs4 import BeautifulSoup


def receiving_dict():
    link = 'https://www.pro-football-reference.com/years/2022/receiving.htm'

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
            targets = row[6]
            receptions = row[7]
            catchPercent = row[8]
            yards = row[9]
            YPR = row[10]
            TDs = row[11]
            YPT = row[14]
            RPG = row[15]
            YPG = row[16]
            Fumbles = row[17]

            for i in range(len(name)-1, 0, -1):
                if name[i] == '*' or name[i] == '+':
                    name = name[:-1]

            playerDic[name.replace(" ", "")] = \
                {
                    'team': team,
                    'targets': targets,
                    'receptions': receptions,
                     'catch%': catchPercent,
                     'yards': yards,
                     'YPR': YPR,
                     'TDs': TDs,
                     'YPT': YPT,
                     'RPG': RPG,
                     'YPG': YPG,
                     'fumbles': Fumbles,
                }

    return playerDic


def beautifulWR(player):
    if player:
        string = "receptions: " + player['receptions'] + ", targets: " + player['targets'] + \
                 ", yards: " + player['yards'] + ", TDs: " + player['TDs']
        return string
