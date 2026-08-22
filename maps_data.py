# -*- coding: utf-8 -*-
"""Карты"""
class Maps:
    def init(self):
        self.maps = {
            'dust2': {'name': 'Dust 2', 'bombsites': ['A', 'B']},
            'mirage': {'name': 'Mirage', 'bombsites': ['A', 'B']},
            'inferno': {'name': 'Inferno', 'bombsites': ['A', 'B']},
            'nuke': {'name': 'Nuke', 'bombsites': ['A', 'B']},
            'train': {'name': 'Train', 'bombsites': ['A', 'B']},
            'sandstone': {'name': 'Sandstone', 'bombsites': []}
        }
    
    def get_map(self, name):
        return self.maps.get(name)