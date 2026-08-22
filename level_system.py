# -*- coding: utf-8 -*-
"""Система уровней"""
import random

class LevelSystem:
    def init(self):
        self.base_exp = 100
        self.exp_multiplier = 1.5
        self.max_level = 100
    
    def calculate_exp_for_level(self, level):
        return int(self.base_exp * (self.exp_multiplier ** (level - 1)))
    
    def get_level_progress(self, current_exp):
        level = 1
        remaining_exp = current_exp
        exp_needed = self.base_exp
        
        while remaining_exp >= exp_needed and level < self.max_level:
            remaining_exp -= exp_needed
            level += 1
            exp_needed = self.calculate_exp_for_level(level)
        
        progress = (remaining_exp / exp_needed) * 100 if exp_needed > 0 else 100
        
        return {
            'level': level,
            'current_exp': remaining_exp,
            'exp_needed': exp_needed,
            'progress': progress
        }
    
    def generate_random_bonus(self, level):
        bonuses = [
            {'type': 'gold', 'name': 'Голда', 'value': random.randint(50, 50 + level * 10)},
            {'type': 'case', 'name': 'Кейс', 'value': 'Обычный'},
            {'type': 'weapon', 'name': 'Оружие', 'value': 'AK-47'},
        ]
        return random.choice(bonuses)