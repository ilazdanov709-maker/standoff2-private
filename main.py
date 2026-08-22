# -*- coding: utf-8 -*-
"""
STANDOFF PRIVATE 2.0 - ИНТЕРФЕЙС В СТИЛЕ STANDOFF 2 0.10.11
"""

# ========== ОТКЛЮЧЕНИЕ ПРЕДУПРЕЖДЕНИЙ ==========
import os
import warnings
warnings.filterwarnings('ignore')
os.environ['KIVY_NO_CONSOLELOG'] = '1'
os.environ['KIVY_NO_ARGS'] = '1'
# ================================================

# ========== НАСТРОЙКА 60 FPS ==========
from kivy.config import Config
Config.set('graphics', 'maxfps', '60')
Config.set('graphics', 'vsync', '1')
Config.set('kivy', 'log_level', 'error')
Config.set('kivy', 'log_enable', '0')
# ========================================

import random
import json
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.progressbar import ProgressBar
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, RoundedRectangle, Line
from kivy.utils import get_color_from_hex

# Импорт модулей
try:
    from bots_system import BotDifficulty, MatchSimulator
    from game_modes import GameModesManager, GameMode
    from maps_data import Maps
    from weapons import Weapons, WeaponType
    from weapons_arcane import ArcaneWeaponCollection, ArcaneWeaponMarketplace
    from database import GameDatabase
    from level_system import LevelSystem
    from skins_system import SkinCollection
    from knives_system import KnifeCollection
    from medals_system import MedalSystem
    from achievements_system import AchievementSystem
    from battle_pass_system import BattlePassSystem
    from daily_rewards import DailyRewardsSystem
    from clan_system import ClanSystem
    from market_system import MarketSystem
    from recoil_system import RecoilSystem
    from kill_feed import KillFeed
    from collections import COLLECTIONS, get_all_collections
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    import sys
    sys.exit(1)

Window.size = (420, 720)
Window.clearcolor = get_color_from_hex('#1a1a1a')

# Цвета
BG_COLOR = get_color_from_hex('#1a1a1a')
BUTTON_COLOR = get_color_from_hex('#2d2d2d')
BUTTON_PRESSED = get_color_from_hex('#3d3d3d')
ACCENT_COLOR = get_color_from_hex('#f0a500')
TEXT_COLOR = get_color_from_hex('#ffffff')
TEXT_SECONDARY = get_color_from_hex('#b0b0b0')
GOLD_COLOR = get_color_from_hex('#f0a500')

class StyledButton(Button):
    def init(self, **kwargs):
        super().init(**kwargs)
        self.background_normal = ''
        self.background_color = BUTTON_COLOR
        self.color = TEXT_COLOR
        self.font_size = dp(14)
        self.bold = True
        self.size_hint_y = None
        self.height = dp(50)
        self.bind(pos=self.update_canvas, size=self.update_canvas)
        with self.canvas.before:
            self.rect_color = Color(*BUTTON_COLOR)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(8)])
            self.border_color = Color(*ACCENT_COLOR)
            self.border = Line(rounded_rectangle=(self.pos[0], self.pos[1], self.size[0], self.size[1], dp(8)), width=1.2)
        self.bind(on_press=self.on_press_style, on_release=self.on_release_style)
    
    def update_canvas(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.border.rounded_rectangle = (self.pos[0], self.pos[1], self.size[0], self.size[1], dp(8))
    
    def on_press_style(self, instance):
        self.rect_color.rgba = BUTTON_PRESSED
    
    def on_release_style(self, instance):
        self.rect_color.rgba = BUTTON_COLORclass StandoffScreen(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=dp(15), spacing=dp(10))
        self.add_widget(self.layout)
        self.setup_header()
    
    def setup_header(self):
        self.header = BoxLayout(orientation='vertical', size_hint_y=0.12)
        self.title_label = Label(
            text='',
            font_size=dp(22),
            bold=True,
            color=TEXT_COLOR,
            size_hint_y=0.6
        )
        self.header.add_widget(self.title_label)
        self.layout.add_widget(self.header)
    
    def set_title(self, text):
        self.title_label.text = text
    
    def add_back_button(self):
        back_btn = StyledButton(
            text='← НАЗАД',
            size_hint_y=None,
            height=dp(40),
            background_color=BUTTON_COLOR
        )
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'menu'))
        self.layout.add_widget(back_btn)

class LoadingScreen(StandoffScreen):
    def init(self, **kwargs):
        super().init(**kwargs)
        self.layout.clear_widgets()
        
        with self.canvas.before:
            Color(*BG_COLOR)
            self.rect = Rectangle(size=Window.size, pos=(0, 0))
        
        logo_layout = FloatLayout(size_hint=(1, 0.6))
        logo = Label(
            text='STANDOFF 2',
            font_size=dp(42),
            bold=True,
            color=ACCENT_COLOR,
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        subtitle = Label(
            text='2 YEARS EDITION  •  v2.0',
            font_size=dp(16),
            color=TEXT_SECONDARY,
            pos_hint={'center_x': 0.5, 'center_y': 0.45}
        )
        logo_layout.add_widget(logo)
        logo_layout.add_widget(subtitle)
        self.layout.add_widget(logo_layout)
        
        self.progress = ProgressBar(
            max=100,
            value=0,
            size_hint=(0.8, 0.04),
            pos_hint={'center_x': 0.5, 'center_y': 0.3}
        )
        self.layout.add_widget(self.progress)
        
        self.status_label = Label(
            text='Загрузка...',
            font_size=dp(12),
            color=TEXT_SECONDARY,
            size_hint=(1, 0.05),
            pos_hint={'center_x': 0.5, 'center_y': 0.22}
        )
        self.layout.add_widget(self.status_label)
        
        self.loading_tasks = [
            'Загрузка баз данных...',
            'Инициализация ботов...',
            'Загрузка оружия...',
            'Загрузка скинов...',
            'Загрузка ножей...',
            'Загрузка медалей...',
            'Загрузка достижений...',
            'Загрузка боевого пропуска...',
            'Загрузка кланов...',
            'Загрузка рынка...',
            'Загрузка коллекций...',
            'Готово!'
        ]
        
        Clock.schedule_interval(self.update_loading, 1.0 / 60.0)
    
    def update_loading(self, dt):
        if self.progress.value < 100:
            self.progress.value += 10 * dt * 60
            task_index = int(self.progress.value / 10)
            if task_index < len(self.loading_tasks):
                self.status_label.text = self.loading_tasks[task_index]
        else:
            Clock.unschedule(self.update_loading)
            Clock.schedule_once(self.go_to_menu, 1)
    
    def go_to_menu(self, dt):
        self.manager.current = 'menu'

class MainMenuScreen(StandoffScreen):
    def init(self, **kwargs):
        super().init(**kwargs)
        self.db = GameDatabase()
        
        self.layout.clear_widgets()
        
        top_panel = BoxLayout(orientation='horizontal', size_hint_y=0.08, spacing=dp(10))
        self.player_info = Label(
            text='👤 Гость',font_size=dp(12),
            color=TEXT_SECONDARY
        )
        self.gold_label = Label(
            text='💰 0',
            font_size=dp(12),
            color=GOLD_COLOR
        )
        self.level_label = Label(
            text='Ур. 1',
            font_size=dp(12),
            color=TEXT_SECONDARY
        )
        top_panel.add_widget(self.player_info)
        top_panel.add_widget(self.gold_label)
        top_panel.add_widget(self.level_label)
        self.layout.add_widget(top_panel)
        
        logo = Label(
            text='STANDOFF 2',
            font_size=dp(32),
            bold=True,
            color=ACCENT_COLOR,
            size_hint_y=0.12
        )
        self.layout.add_widget(logo)
        
        self.username_input = TextInput(
            hint_text='Введите имя игрока',
            multiline=False,
            font_size=dp(13),
            size_hint_y=None,
            height=dp(40),
            background_color=get_color_from_hex('#2d2d2d'),
            foreground_color=TEXT_COLOR,
            hint_text_color=TEXT_SECONDARY,
            padding=[dp(10), dp(10)]
        )
        self.layout.add_widget(self.username_input)
        
        scroll = ScrollView(size_hint_y=0.6)
        self.buttons_layout = GridLayout(
            cols=2,
            spacing=dp(10),
            padding=dp(5),
            size_hint_y=None
        )
        self.buttons_layout.bind(minimum_height=self.buttons_layout.setter('height'))
        
        menu_items = [
            ('📝 ПРОФИЛЬ', self.create_profile),
            ('📂 ЗАГРУЗИТЬ', self.load_profile),
            ('🤖 БОТЫ', lambda x: setattr(self.manager, 'current', 'bots')),
            ('🎮 РЕЖИМЫ', lambda x: setattr(self.manager, 'current', 'modes')),
            ('🗺️ КАРТЫ', lambda x: setattr(self.manager, 'current', 'maps')),
            ('📋 РАССТАНОВКА', lambda x: setattr(self.manager, 'current', 'setup')),
            ('📊 УРОВЕНЬ', lambda x: setattr(self.manager, 'current', 'level')),
            ('🏅 МЕДАЛИ', lambda x: setattr(self.manager, 'current', 'medals')),
            ('🎯 ДОСТИЖЕНИЯ', lambda x: setattr(self.manager, 'current', 'achievements')),
            ('📅 ЕЖЕДНЕВНЫЕ', lambda x: setattr(self.manager, 'current', 'daily')),
            ('🎁 КЕЙСЫ', lambda x: setattr(self.manager, 'current', 'cases')),
            ('🔫 ОРУЖИЕ', lambda x: setattr(self.manager, 'current', 'weapons')),
            ('✨ ARCANE', lambda x: setattr(self.manager, 'current', 'arcane')),
            ('🔪 НОЖИ', lambda x: setattr(self.manager, 'current', 'knives')),
            ('💎 РЫНОК', lambda x: setattr(self.manager, 'current', 'market')),
            ('👥 КЛАНЫ', lambda x: setattr(self.manager, 'current', 'clans')),
            ('📅 БОЕВОЙ ПРОПУСК', lambda x: setattr(self.manager, 'current', 'battlepass')),
        ]
        
        for text, callback in menu_items:
            btn = StyledButton(
                text=text,
                size_hint_y=None,
                height=dp(60),
                halign='center',
                valign='middle'
            )
            btn.bind(on_press=callback)
            self.buttons_layout.add_widget(btn)
        
        scroll.add_widget(self.buttons_layout)
        self.layout.add_widget(scroll)
    
    def create_profile(self, instance):
        username = self.username_input.text.strip()
        if not username:
            self.show_popup('Ошибка', 'Введите имя')
            return
        if self.db.create_player(username):
            self.player_info.text = f'👤 {username}'
            self.gold_label.text = '💰 100'
            self.level_label.text = 'Ур. 1'
            self.show_popup('Успех', f'Профиль {username} создан!')
        else:
            self.show_popup('Ошибка', 'Имя уже занято')def load_profile(self, instance):
        username = self.username_input.text.strip()
        if not username:
            self.show_popup('Ошибка', 'Введите имя')
            return
        player = self.db.get_player(username)
        if player:
            self.player_info.text = f'👤 {player["username"]}'
            self.gold_label.text = f'💰 {player["gold"]}'
            self.level_label.text = f'Ур. {player["level"]}'
            self.show_popup('Профиль', f'Игрок: {player["username"]}\nГолда: {player["gold"]}')
        else:
            self.show_popup('Ошибка', 'Профиль не найден')
    
    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message, color=TEXT_COLOR),
            size_hint=(0.8, 0.4),
            background='',
            title_color=ACCENT_COLOR
        )
        popup.open()

class CasesScreen(StandoffScreen):
    """Экран кейсов с коллекциями из 0.10.11"""
    def init(self, **kwargs):
        super().init(**kwargs)
        self.set_title('🎁 КЕЙСЫ И КОЛЛЕКЦИИ')
        scroll = ScrollView(size_hint_y=0.7)
        content = BoxLayout(orientation='vertical', size_hint_y=None, spacing=dp(10))
        content.bind(minimum_height=content.setter('height'))
        
        for collection in COLLECTIONS:
            btn = StyledButton(
                text=collection.name,
                size_hint_y=None,
                height=dp(50),
                font_size=dp(16)
            )
            btn.bind(on_press=lambda x, c=collection: self.open_case(c))
            content.add_widget(btn)
        
        scroll.add_widget(content)
        self.layout.add_widget(scroll)
        self.add_back_button()
    
    def open_case(self, collection):
        skin = random.choice(collection.skins)
        popup = Popup(
            title='Открытие кейса',
            content=Label(
                text=f"Вы получили:\n{skin['weapon']} | {skin['name']}\nРедкость: {skin['rarity']}",
                color=TEXT_COLOR
            ),
            size_hint=(0.8, 0.4),
            background='',
            title_color=ACCENT_COLOR
        )
        popup.open()

class SimpleScreen(StandoffScreen):
    def init(self, title, **kwargs):
        super().init(**kwargs)
        self.set_title(title)
        self.add_back_button()

class StandoffApp(App):
    def build(self):
        self.title = 'Standoff 2 - 2 years v2.0'
        
        sm = ScreenManager()
        sm.add_widget(LoadingScreen(name='loading'))
        sm.add_widget(MainMenuScreen(name='menu'))
        
        screens = [
            ('bots', '🤖 ИГРА С БОТАМИ'),
            ('modes', '🎮 РЕЖИМЫ ИГРЫ'),
            ('maps', '🗺️ КАРТЫ'),
            ('setup', '📋 РАССТАНОВКА'),
            ('level', '📊 УРОВЕНЬ'),
            ('medals', '🏅 МЕДАЛИ'),
            ('achievements', '🎯 ДОСТИЖЕНИЯ'),
            ('daily', '📅 ЕЖЕДНЕВНЫЕ НАГРАДЫ'),
            ('cases', '🎁 КЕЙСЫ'),
            ('weapons', '🔫 ОРУЖИЕ'),
            ('arcane', '✨ ARCANE ОРУЖИЕ'),
            ('knives', '🔪 НОЖИ'),
            ('market', '💎 РЫНОК'),
            ('clans', '👥 КЛАНЫ'),
            ('battlepass', '📅 БОЕВОЙ ПРОПУСК'),
        ]
        
        for name, title in screens:
            if name == 'cases':
                sm.add_widget(CasesScreen(name=name))
            else:
                sm.add_widget(SimpleScreen(name=name, title=title))
        
        sm.current = 'loading'
        return sm

if name == 'main':
    StandoffApp().run()