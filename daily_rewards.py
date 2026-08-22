# -*- coding: utf-8 -*-
"""Ежедневные награды"""
from datetime import datetime, timedelta

class DailyRewardsSystem:
    def init(self):
        self.rewards = [100, 150, 200, 250, 300, 400, 500]
        self.current_day = 0
        self.last_claim = None
    
    def can_claim(self):
        if self.last_claim is None:
            return True
        return datetime.now() - self.last_claim >= timedelta(days=1)
    
    def claim(self):
        if not self.can_claim():
            return None
        reward = self.rewards[self.current_day]
        self.current_day = (self.current_day + 1) % len(self.rewards)
        self.last_claim = datetime.now()
        return reward