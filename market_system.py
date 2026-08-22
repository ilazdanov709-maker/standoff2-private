# -*- coding: utf-8 -*-
"""Система рынка"""
import random

class MarketListing:
    def init(self, item, price, seller):
        self.item = item
        self.price = price
        self.seller = seller
        self.id = random.randint(1000, 9999)

class MarketSystem:
    def init(self):
        self.listings = []
    
    def add_listing(self, item, price, seller):
        listing = MarketListing(item, price, seller)
        self.listings.append(listing)
        return listing
    
    def get_sorted_listings(self):
        return sorted(self.listings, key=lambda x: x.price)