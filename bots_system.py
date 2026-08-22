# -*- coding: utf-8 -*-
"""Система ботов"""
import random
from enum import Enum

class BotDifficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    EXPERT = "expert"

class Bot:
    def init(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.health = 100
        self.weapon = self.select_weapon()
        self.skill_level = self.set_skill()
        self.accuracy = self.set_accuracy()
    
    def select_weapon(self):
        weapons = {
            BotDifficulty.EASY: ['P90', 'MP5', 'Glock-18'],
            BotDifficulty.MEDIUM: ['AK-47', 'M4A1', 'FAMAS'],
            BotDifficulty.HARD: ['AWP', 'AK-47', 'M4A4'],
            BotDifficulty.EXPERT: ['AWM', 'AWP', 'M-40', 'Desert Eagle']
        }
        return random.choice(weapons[self.difficulty])
    
    def set_skill(self):
        skills = {
            BotDifficulty.EASY: random.randint(10, 30),
            BotDifficulty.MEDIUM: random.randint(30, 50),
            BotDifficulty.HARD: random.randint(50, 70),
            BotDifficulty.EXPERT: random.randint(70, 90)
        }
        return skills[self.difficulty]
    
    def set_accuracy(self):
        accuracy = {
            BotDifficulty.EASY: random.uniform(0.2, 0.4),
            BotDifficulty.MEDIUM: random.uniform(0.4, 0.6),
            BotDifficulty.HARD: random.uniform(0.6, 0.8),
            BotDifficulty.EXPERT: random.uniform(0.8, 0.95)
        }
        return accuracy[self.difficulty]
    
    def shoot(self, distance):
        hit_chance = self.accuracy * (1 - distance / 100)
        if random.random() < hit_chance:
            return {"hit": True, "damage": random.randint(15, 40)}
        return {"hit": False, "damage": 0}

class MatchSimulator:
    def init(self, player_name, bot_difficulty):
        self.player_name = player_name
        self.bot_difficulty = bot_difficulty
        self.bots = [Bot(f"Bot_{i+1}", bot_difficulty) for i in range(5)]
        self.player_kills = 0
        self.rounds_won = 0
        self.rounds_lost = 0
    
    def start_match(self):
        for _ in range(13):
            won = random.random() > 0.5
            if won:
                self.rounds_won += 1
                self.player_kills += random.randint(0, 5)
            else:
                self.rounds_lost += 1
        return {
            'won': self.rounds_won > self.rounds_lost,
            'kills': self.player_kills,
            'rounds_won': self.rounds_won,
            'rounds_lost': self.rounds_lost
        }