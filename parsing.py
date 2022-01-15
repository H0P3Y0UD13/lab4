from os import write
from bs4 import BeautifulSoup
import csv
import requests
import random


def parsing_hero():
    with requests.session() as se:
        se.headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43',
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7"
        }
    url = "https://dota2.ru/heroes/"
    r = se.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find(id="project-dota2")
    heroes_all = results.find_all("div", class_="base-hero__block")
    strength = []
    agility = []
    intelligence = []
    POINT = 0
    for x in heroes_all:
        POINT += 1
        heroes_a = x.find("div", class_="base-hero__block-hero")
        y = str(heroes_a.text)
        y = y.replace(" ","")
        y = y.replace("\n","")
        y = y.replace("\r",",")
        if POINT == 1:
            strength = (y.split(','))
        if POINT == 2:
            agility = (y.split(','))
        if POINT == 3:
            intelligence = (y.split(','))
    strength.remove('')
    agility.remove('')
    intelligence.remove('')

    spell_list = []
    for I in range(1, 7):
        url =  "http://www.fatalgame.com/skill/dota2/" + str(I) + "/"
        r = se.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find(id="rexpage")
        spells_all = results.find("div", class_ = "skilslist_items")
        for x in spells_all:
            spell = x.text.replace("/", "")
            cl_spell = "".join((x for x in spell if not x.isdigit()))
            spell_list.append(cl_spell)

    with open("dota2.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["Атрибут", "Герой", "Damage", "Cпособности"])
        I = 0
        for x in strength:
            I +=3
            file_writer.writerow(["Сила", x, str(random.randrange(30,70)), str(spell_list[I]) + ', ' + str(spell_list[I-1]) + ', ' + str(spell_list[I-2])])
        for x in agility:
            I += 3
            file_writer.writerow(["Ловкость", x, str(random.randrange(30,70)), str(spell_list[I]) + ', ' + str(spell_list[I-1]) + ', ' + str(spell_list[I-2])])
        for x in intelligence:
            I += 3
            file_writer.writerow(["Интеллект", x, str(random.randrange(30,70)), str(spell_list[I]) + ', ' + str(spell_list[I-1]) + ', ' + str(spell_list[I-2])])
    return(strength, agility, intelligence)