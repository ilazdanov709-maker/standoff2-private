# -*- coding: utf-8 -*-
"""Боевой пропуск"""
import random

class BattlePass:
    def init(self):
        self.levels = 50
        self.current_level = 1
        self.is_premium = False
        self.free_rewards = {level: random.randint(50, 100) for level in range(1, 51)}
        self.premium_rewards = {level: random.randint(200, 500) for level in range(1, 51)}
    
    def level_up(self):
        if self.current_level < self.levels:
            self.current_level += 1
            return True
        return False

class BattlePassSystem:
    def init(self):
        self.battle_pass = BattlePass()
        self.premium_price = 500