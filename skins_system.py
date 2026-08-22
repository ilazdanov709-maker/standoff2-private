# -*- coding: utf-8 -*-
"""Система скинов"""
import random
from enum import Enum

class SkinRarity(Enum):
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"

class WeaponSkin:
    def init(self, name, weapon, rarity):
        self.name = name
        self.weapon = weapon
        self.rarity = rarity
        self.stattrak = random.random() < 0.1
    
    def get_description(self):
        return f"{self.name} ({self.weapon})"

class SkinCollection:
    def init(self):
        self.skins = {
            'ak47': [
                WeaponSkin('AK-47 | Красная линия', 'AK-47', SkinRarity.RARE),
                WeaponSkin('AK-47 | Неон', 'AK-47', SkinRarity.EPIC),
            ]
        }
    
    def get_skin_for_weapon(self, weapon):
        if weapon in self.skins:
            return random.choice(self.skins[weapon])
        return None