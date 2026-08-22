# -*- coding: utf-8 -*-
"""Система достижений"""
from enum import Enum

class AchievementType(Enum):
    KILLS = "kills"
    WINS = "wins"
    HEADSHOTS = "headshots"
    GOLD = "gold"

class Achievement:
    def init(self, name, achievement_type, target, reward_gold, icon):
        self.name = name
        self.achievement_type = achievement_type
        self.target = target
        self.reward_gold = reward_gold
        self.icon = icon
        self.progress = 0
        self.completed = False

class AchievementSystem:
    def init(self):
        self.achievements = [
            Achievement('Первая кровь', AchievementType.KILLS, 1, 50, '🔪'),
            Achievement('Убийца', AchievementType.KILLS, 100, 500, '⚔️'),
            Achievement('Победитель', AchievementType.WINS, 10, 300, '🏆'),
            Achievement('Богач', AchievementType.GOLD, 10000, 1000, '💰'),
        ]