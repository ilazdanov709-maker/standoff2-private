# -*- coding: utf-8 -*-
"""Оружие с параметрами отдачи"""
from enum import Enum

class WeaponType(Enum):
    PISTOL = "pistol"
    SMG = "smg"
    RIFLE = "rifle"
    SNIPER = "sniper"

class Weapon:
    def init(self, name, weapon_type, damage, accuracy, price,
                 recoil_vertical, recoil_horizontal, recoil_recovery,
                 recoil_pattern=None):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.accuracy = accuracy
        self.price = price
        self.recoil_vertical = recoil_vertical
        self.recoil_horizontal = recoil_horizontal
        self.recoil_recovery = recoil_recovery
        self.recoil_pattern = recoil_pattern or []
    
    def get_info(self):
        return {
            'name': self.name,
            'type': self.weapon_type.value,
            'damage': self.damage,
            'accuracy': self.accuracy,
            'price': self.price,
            'recoil_vertical': self.recoil_vertical,
            'recoil_horizontal': self.recoil_horizontal,
        }

class Weapons:
    def init(self):
        self.weapons = {
            'glock18': Weapon('Glock-18', WeaponType.PISTOL, 15, 0.7, 200, 2.0, 0.5, 0.9),
            'p350': Weapon('P-350', WeaponType.PISTOL, 30, 0.82, 550, 3.0, 0.8, 0.85),
            'deagle': Weapon('Desert Eagle', WeaponType.PISTOL, 45, 0.85, 700, 6.0, 2.0, 0.7),
            'mp5': Weapon('MP5', WeaponType.SMG, 18, 0.6, 500, 1.5, 0.6, 0.95),
            'p90': Weapon('P90', WeaponType.SMG, 20, 0.55, 600, 1.8, 0.7, 0.9),
            'ak47': Weapon('AK-47', WeaponType.RIFLE, 35, 0.7, 1000, 4.5, 1.5, 0.6,
                           [(0,-1),(0,-2),(-1,-3),(1,-4),(0,-5),(-2,-6),(2,-7),(-1,-8),(1,-9),(0,-10)]),
            'm4a1': Weapon('M4A1', WeaponType.RIFLE, 30, 0.75, 1000, 3.8, 1.2, 0.65,
                           [(0,-1),(0,-2),(0,-3),(-1,-4),(1,-5),(0,-6),(-1,-7),(1,-8),(0,-9),(0,-10)]),
            'awp': Weapon('AWP', WeaponType.SNIPER, 80, 0.9, 2000, 10.0, 3.0, 0.3),
            'awm': Weapon('AWM', WeaponType.SNIPER, 85, 0.92, 2500, 12.0, 3.5, 0.25),
            'm40': Weapon('M-40', WeaponType.SNIPER, 70, 0.88, 1800, 8.0, 2.5, 0.4)
        }
    
    def get_weapon(self, name):
        return self.weapons.get(name.lower())
    
    def get_all_weapons(self):
        return self.weapons