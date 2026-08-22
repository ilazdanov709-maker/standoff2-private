# -*- coding: utf-8 -*-
"""Система отдачи"""
import random

class RecoilSystem:
    def init(self, weapon):
        self.weapon = weapon
        self.pattern = weapon.recoil_pattern
        self.pattern_index = 0
        self.current_offset_x = 0.0
        self.current_offset_y = 0.0
        self.last_shot_time = 0
    
    def get_next_offset(self, dt=0.016):
        # Восстановление
        if self.last_shot_time > 0:
            recovery = self.weapon.recoil_recovery * dt * 10
            self.current_offset_x *= (1 - recovery)
            self.current_offset_y *= (1 - recovery)
        
        if self.pattern and self.pattern_index < len(self.pattern):
            dx, dy = self.pattern[self.pattern_index]
            self.pattern_index += 1
            dx += random.uniform(-0.2, 0.2) * self.weapon.recoil_horizontal
            dy += random.uniform(-0.2, 0.2) * self.weapon.recoil_vertical
        else:
            dx = random.uniform(-self.weapon.recoil_horizontal, self.weapon.recoil_horizontal)
            dy = random.uniform(0, self.weapon.recoil_vertical)
        
        self.current_offset_x += dx
        self.current_offset_y += dy
        self.last_shot_time = 1
        return self.current_offset_x, self.current_offset_y
    
    def reset(self):
        self.current_offset_x = 0.0
        self.current_offset_y = 0.0
        self.pattern_index = 0
        self.last_shot_time = 0