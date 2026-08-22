# -*- coding: utf-8 -*-
"""Режимы игры"""
import random
from enum import Enum

class GameMode(Enum):
    BOMB_PLANT = "bomb_plant"
    TEAM_DEATHMATCH = "team_deathmatch"
    ARMS_RACE = "arms_race"
    SNIPER_BATTLE = "sniper_battle"

class GameModesManager:
    def init(self):
        self.current_mode = None
    
    def get_mode_name(self, mode):
        names = {
            GameMode.BOMB_PLANT: "Закладка бомбы",
            GameMode.TEAM_DEATHMATCH: "Командный бой",
            GameMode.ARMS_RACE: "Гонка вооружения",
            GameMode.SNIPER_BATTLE: "Битва снайперов"
        }
        return names.get(mode, "Неизвестно")