import requests
import pandas as pd
from bs4 import BeautifulSoup


def passing_dict():
    link = 'https://www.pro-football-reference.com/years/2022/passing.htm'

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
            completions = row[7]
            attempts = row[8]
            compPercent = row[9]
            yards = row[10]
            TDs = row[11]
            TDPercent = row[12]
            int = row[13]
            intPercent = row[14]
            YPA = row[17]
            YPC = row[19]

            for i in range(len(name)-1, 0, -1):
                if name[i] == '*' or name[i] == '+':
                    name = name[:-1]

            playerDic[name.replace(" ", "")] = {'team': team,
                               'completions': completions,
                               'attempts': attempts,
                               'comp%': compPercent,
                               'yards': yards,
                               'TDs': TDs,
                               'TD%': TDPercent,
                               'int': int,
                               'int%': intPercent,
                               'YPA': YPA,
                               'YPC': YPC
                               }

    return playerDic


def beautifulQB(player):
    if player:
        string = "completions: " + player['completions'] + ", attempts: " + player['attempts'] + \
                 ", yards: " + player['yards'] + ", TDs: " + player['TDs'] + ", ints: " + player['int']
        return string
