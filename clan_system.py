# -*- coding: utf-8 -*-
"""Система кланов"""
class Clan:
    def init(self, name, tag, leader):
        self.name = name
        self.tag = tag
        self.leader = leader
        self.members = [leader]
        self.level = 1

class ClanSystem:
    def init(self):
        self.clans = []
    
    def create_clan(self, name, tag, leader):
        clan = Clan(name, tag, leader)
        self.clans.append(clan)
        return clan