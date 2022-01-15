from classes import Gods, Str_heroes
from classes import Agl_heroes
from classes import Int_heroes
from classes import Heroes
from parsing import parsing_hero
import csv


parsing_hero()
with open("dota2.csv", encoding="utf-8") as File:  
    reader = csv.reader(File)
    for row in reader:
        if row[1] == "Zeus":
            ultra_spell = "*Bang!*"
            hero = Gods(row[0], row[1], row[2], row[3], ultra_spell)
            hero.show_data()
            hero.use_spell()
            hero.show_the_divine()
            continue
        elif row[0] == "Сила":
            hero = Str_heroes(row[0], row[1], row[2], row[3])
            hero.show_data()
            hero.use_spell()
        elif row[0] == "Ловкость":
            hero = Agl_heroes(row[0], row[1], row[2], row[3])
            hero.show_data()
            hero.use_spell()
        elif row[0] == "Интеллект":
            hero = Int_heroes(row[0], row[1], row[2], row[3])
            hero.show_data()
            hero.use_spell()
