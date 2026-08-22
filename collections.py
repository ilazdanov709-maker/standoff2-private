# -*- coding: utf-8 -*-
"""Все коллекции скинов из Standoff 2 0.10.11"""

class Collection:
    def init(self, name, description, skins):
        self.name = name
        self.description = description
        self.skins = skins

COLLECTIONS = [
    Collection("Классика", "Классические скины для опытных бойцов", [
        {"weapon": "AK-47", "name": "AK-47 | Классика", "rarity": "common", "pattern": "classic"},
        {"weapon": "M4A1", "name": "M4A1 | Классика", "rarity": "common", "pattern": "classic"},
        {"weapon": "Glock-18", "name": "Glock-18 | Классика", "rarity": "common", "pattern": "classic"},
        {"weapon": "USP", "name": "USP | Классика", "rarity": "common", "pattern": "classic"},
        {"weapon": "P250", "name": "P250 | Классика", "rarity": "uncommon", "pattern": "classic"},
    ]),
    Collection("Дракон", "Скины с восточной тематикой", [
        {"weapon": "AK-47", "name": "AK-47 | Дракон", "rarity": "epic", "pattern": "dragon"},
        {"weapon": "M4A4", "name": "M4A4 | Дракон", "rarity": "epic", "pattern": "dragon"},
        {"weapon": "AWP", "name": "AWP | Дракон", "rarity": "legendary", "pattern": "dragon"},
        {"weapon": "Desert Eagle", "name": "Desert Eagle | Дракон", "rarity": "rare", "pattern": "dragon"},
        {"weapon": "P90", "name": "P90 | Дракон", "rarity": "rare", "pattern": "dragon"},
    ]),
    Collection("Ледяной", "Холодные скины из льда и снега", [
        {"weapon": "AK-47", "name": "AK-47 | Ледяной", "rarity": "epic", "pattern": "ice"},
        {"weapon": "M4A1", "name": "M4A1 | Ледяной", "rarity": "epic", "pattern": "ice"},
        {"weapon": "AWP", "name": "AWP | Ледяной", "rarity": "legendary", "pattern": "ice"},
        {"weapon": "Glock-18", "name": "Glock-18 | Ледяной", "rarity": "rare", "pattern": "ice"},
        {"weapon": "MP5", "name": "MP5 | Ледяной", "rarity": "rare", "pattern": "ice"},
    ]),
    Collection("Кровавый", "Мрачные скины с кровавыми узорами", [
        {"weapon": "AK-47", "name": "AK-47 | Кровавый", "rarity": "epic", "pattern": "blood"},
        {"weapon": "M4A1", "name": "M4A1 | Кровавый", "rarity": "epic", "pattern": "blood"},
        {"weapon": "P250", "name": "P250 | Кровавый", "rarity": "rare", "pattern": "blood"},
        {"weapon": "AWP", "name": "AWP | Кровавый", "rarity": "legendary", "pattern": "blood"},
        {"weapon": "Knife", "name": "Knife | Кровавая паутина", "rarity": "legendary", "pattern": "blood_web"},
    ]),
    Collection("Феникс", "Огненные скины, возрождающиеся из пепла", [
        {"weapon": "AK-47", "name": "AK-47 | Феникс", "rarity": "epic", "pattern": "phoenix"},
        {"weapon": "M4A4", "name": "M4A4 | Феникс", "rarity": "epic", "pattern": "phoenix"},
        {"weapon": "Desert Eagle", "name": "Desert Eagle | Феникс", "rarity": "rare", "pattern": "phoenix"},
        {"weapon": "P90", "name": "P90 | Феникс", "rarity": "rare", "pattern": "phoenix"},
    ]),
    Collection("Неон", "Яркие неоновые скины", [
        {"weapon": "AK-47", "name": "AK-47 | Неон", "rarity": "epic", "pattern": "neon"},
        {"weapon": "M4A1", "name": "M4A1 | Неон", "rarity": "epic", "pattern": "neon"},
        {"weapon": "P90", "name": "P90 | Неон", "rarity": "rare", "pattern": "neon"},
        {"weapon": "Glock-18", "name": "Glock-18 | Неон", "rarity": "rare", "pattern": "neon"},
        {"weapon": "AWP", "name": "AWP | Неон", "rarity": "legendary", "pattern": "neon"},
    ]),
    Collection("Пустынный", "Камуфляж для пустынных операций", [
        {"weapon": "AK-47", "name": "AK-47 | Пустынный", "rarity": "uncommon", "pattern": "desert"},
        {"weapon": "M4A1", "name": "M4A1 | Пустынный", "rarity": "uncommon", "pattern": "desert"},
        {"weapon": "P250", "name": "P250 | Пустынный", "rarity": "common", "pattern": "desert"},
        {"weapon": "MP5", "name": "MP5 | Пустынный", "rarity": "uncommon", "pattern": "desert"},
    ]),
    Collection("Золотой", "Роскошные золотые скины", [
        {"weapon": "AK-47", "name": "AK-47 | Золотой", "rarity": "legendary", "pattern": "gold"},
        {"weapon": "M4A1", "name": "M4A1 | Золотой", "rarity": "legendary", "pattern": "gold"},
        {"weapon": "AWP", "name": "AWP | Золотой", "rarity": "legendary", "pattern": "gold"},
        {"weapon": "Desert Eagle", "name": "Desert Eagle | Золотой", "rarity": "legendary", "pattern": "gold"},
        {"weapon": "Knife", "name": "Knife | Золотой", "rarity": "legendary", "pattern": "gold"},
    ]),
    Collection("Кибер", "Футуристические скины в стиле киберпанк", [
        {"weapon": "AK-47", "name": "AK-47 | Кибер", "rarity": "epic", "pattern": "cyber"},
        {"weapon": "M4A1", "name": "M4A1 | Кибер", "rarity": "epic", "pattern": "cyber"},
        {"weapon": "P90", "name": "P90 | Кибер", "rarity": "rare", "pattern": "cyber"},
        {"weapon": "AWP", "name": "AWP | Кибер", "rarity": "legendary", "pattern": "cyber"},
    ]),
    Collection("Мистик", "Таинственные скины с мистическими символами", [
        {"weapon": "AK-47", "name": "AK-47 | Мистик", "rarity": "epic", "pattern": "mystic"},
        {"weapon": "M4A4", "name": "M4A4 | Мистик", "rarity": "epic", "pattern": "mystic"},
        {"weapon": "Desert Eagle", "name": "Desert Eagle | Мистик", "rarity": "rare", "pattern": "mystic"},
        {"weapon": "Glock-18", "name": "Glock-18 | Мистик", "rarity": "rare", "pattern": "mystic"},
    ]),
    Collection("Легенда", "Скины для настоящих легенд", [
        {"weapon": "AK-47", "name": "AK-47 | Легенда", "rarity": "legendary", "pattern": "legend"},
        {"weapon": "AWP", "name": "AWP | Легенда", "rarity": "legendary", "pattern": "legend"},
        {"weapon": "M4A1", "name": "M4A1 | Легенда", "rarity": "legendary", "pattern": "legend"},
    ]),
    Collection("Подарочный набор 2020", "Праздничные скины к новому году", [
        {"weapon": "AK-47", "name": "AK-47 | Новый год", "rarity": "epic", "pattern": "newyear"},
        {"weapon": "M4A1", "name": "M4A1 | Новый год", "rarity": "epic", "pattern": "newyear"},
        {"weapon": "Glock-18", "name": "Glock-18 | Новый год", "rarity": "rare", "pattern": "newyear"},
        {"weapon": "P250", "name": "P250 | Новый год", "rarity": "rare", "pattern": "newyear"},
    ]),
]

def get_all_collections():
    return COLLECTIONS

def get_collection_by_name(name):
    for c in COLLECTIONS:
        if c.name == name:
            return c
    return None