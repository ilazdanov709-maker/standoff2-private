# -*- coding: utf-8 -*-
"""Arcane оружие"""
import random

class WeaponRarity:
    ARCANE = "arcane"

class ArcaneWeaponSkin:
    def init(self, name, weapon, price, effect):
        self.name = name
        self.weapon = weapon
        self.rarity = WeaponRarity.ARCANE
        self.price = price
        self.effect = effect
        self.glow_color = random.choice(['purple', 'gold', 'blue', 'red', 'white'])
    
    def get_full_name(self):
        return f"✨ {self.name} ✨"

class ArcaneWeaponCollection:
    def init(self):
        self.arcane_skins = {
            'ak47': [
                ArcaneWeaponSkin('AK-47 | Космос', 'AK-47', 10000, 'Галактическое свечение'),
                ArcaneWeaponSkin('AK-47 | Абсолют', 'AK-47', 25000, 'Абсолютная мощь'),
            ],
            'awm': [
                ArcaneWeaponSkin('AWM | Космос', 'AWM', 15000, 'Галактическое свечение'),
                ArcaneWeaponSkin('AWM | Абсолют', 'AWM', 35000, 'Абсолютная мощь'),
            ]
        }
    
    def get_all_arcane_skins(self):
        all_skins = []
        for skins in self.arcane_skins.values():
            all_skins.extend(skins)
        return all_skins

class ArcaneWeaponMarketplace:
    def init(self):
        self.collection = ArcaneWeaponCollection()
        self.listings = []
        for skin in self.collection.get_all_arcane_skins():
            self.listings.append({'skin': skin, 'price': skin.price})
    
    def sort_by_price_descending(self):
        return sorted(self.listings, key=lambda x: x['price'], reverse=True)