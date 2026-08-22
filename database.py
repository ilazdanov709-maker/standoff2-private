# -*- coding: utf-8 -*-
"""База данных"""
import sqlite3
import json

class GameDatabase:
    def init(self, db_name='standoff.db'):
        self.db_name = db_name
        self.init_tables()
    
    def get_connection(self):
        return sqlite3.connect(self.db_name)
    
    def init_tables(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                gold INTEGER DEFAULT 100,
                level INTEGER DEFAULT 1,
                exp INTEGER DEFAULT 0,
                inventory TEXT DEFAULT '[]',
                medals TEXT DEFAULT '[]',
                achievements TEXT DEFAULT '[]',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_player(self, username):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO players (username) VALUES (?)", (username,))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()
    
    def get_player(self, username):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM players WHERE username = ?", (username,))
        player = cursor.fetchone()
        conn.close()
        
        if player:
            return {
                'id': player[0],
                'username': player[1],
                'gold': player[2],
                'level': player[3],
                'exp': player[4],
                'inventory': json.loads(player[5]),
                'medals': json.loads(player[6]),
                'achievements': json.loads(player[7])
            }
        return None