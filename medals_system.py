# -*- coding: utf-8 -*-
"""Система медалей"""
from enum import Enum

class MedalRarity(Enum):
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"
    PLATINUM = "platinum"
    DIAMOND = "diamond"
    LEGENDARY = "legendary"
    MYTHIC = "mythic"
    DIVINE = "divine"

class Medal:
    def init(self, name, rarity, level_required, icon):
        self.name = name
        self.rarity = rarity
        self.level_required = level_required
        self.icon = icon

class MedalSystem:
    def init(self):
        self.medals = {
            10: Medal('Бронзовая звезда', MedalRarity.BRONZE, 10, '🥉'),
            20: Medal('Серебряная звезда', MedalRarity.SILVER, 20, '🥈'),
            30: Medal('Золотая звезда', MedalRarity.GOLD, 30, '🥇'),
            40: Medal('Платиновая звезда', MedalRarity.PLATINUM, 40, '💎'),
            50: Medal('Алмазная звезда', MedalRarity.DIAMOND, 50, '💠'),
            60: Medal('Легендарная звезда', MedalRarity.LEGENDARY, 60, '🌟'),
            70: Medal('Мифическая звезда', MedalRarity.MYTHIC, 70, '🔮'),
            80: Medal('Божественная звезда', MedalRarity.DIVINE, 80, '⚡'),
            90: Medal('Космическая звезда', MedalRarity.DIVINE, 90, '🌌'),
            100: Medal('Абсолютная звезда', MedalRarity.DIVINE, 100, '👑')
        }