# -*- coding: utf-8 -*-
"""Ножи (только Arcane)"""
import random
from enum import Enum

class KnifeType(Enum):
    M9 = "m9_bayonet"
    BUTTERFLY = "butterfly"
    JKOMANDO = "jkomando"

class KnifeSkinRarity(Enum):
    ARCANE = "arcane"

class KnifeSkin:
    def init(self, name, knife_type, price):
        self.name = name
        self.knife_type = knife_type
        self.rarity = KnifeSkinRarity.ARCANE
        self.price = price
        self.glow_effect = random.choice(['purple', 'gold', 'blue'])
    
    def get_full_name(self):
        return f"✨ {self.name} ✨"

class KnifeCollection:
    def init(self):
        self.knives = {
            KnifeType.M9: [
                KnifeSkin('M9 | Космос', KnifeType.M9, 10000),
                KnifeSkin('M9 | Абсолют', KnifeType.M9, 50000),
            ],
            KnifeType.BUTTERFLY: [
                KnifeSkin('Butterfly | Галактика', KnifeType.BUTTERFLY, 10000),
                KnifeSkin('Butterfly | Абсолют', KnifeType.BUTTERFLY, 60000),
            ],
            KnifeType.JKOMANDO: [
                KnifeSkin('JKomando | Пустота', KnifeType.JKOMANDO, 10000),
                KnifeSkin('JKomando | Абсолют', KnifeType.JKOMANDO, 50000),
            ]
        }
    
    def get_all_arcane_skins(self):
        all_skins = []
        for skins in self.knives.values():
            all_skins.extend(skins)
        return all_skins