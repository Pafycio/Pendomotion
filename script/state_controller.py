__author__ = 'Pawel'

import pygame
from copy import copy
from menu_state import Menu
from create_game_state import CreateGame
from game_state import Game
from game_menu_state import GameMenu
from music_controller import MusicController


class StateController(object):
    """
    STATE CONTROLLER
    """
    def __init__(self, api, surf):
        self.api = api
        self.surf = surf
        self.music = MusicController()
        self.state = Menu(surf, None)
        self.music.play_music()

    def state_handler(self):
        for event in pygame.event.get():
            value = self.state.on_event(event)
            self.change_state(value)

        self.state.on_update()
        self.state.on_render()

    def change_state(self, value):
        if value == "NONE":
            pass
        elif value == "EXIT":
            self.api.running = False
        elif value == "PREV":
            self.state = self.state.get_prev()
        elif value == "MENU":
            self.state = Menu(self.surf, copy(self.state))
        elif value == "CREATE":
            self.state = CreateGame(self.surf, copy(self.state))
        elif value == "GAME":
            self.music.set_volume(50)
            self.state = Game(self.surf, copy(self.state))
        elif value == "PAUSE":
            self.state = GameMenu(self.surf, copy(self.state))
        elif value == "MUSIC_PLAY":
            self.music.play_music()
        elif value == "MUSIC_PAUSE":
            self.music.pause_music()
        elif value == "MUSIC_UN_PAUSE":
            self.music.un_pause_music()