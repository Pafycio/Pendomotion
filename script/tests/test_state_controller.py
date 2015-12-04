__author__ = 'Pawel'
# -*- coding: utf-8 -*-

import unittest
from script import main_api
from script import state_controller
from script.map import Map
from script import menu_state
from script import game_menu_state
from script import game_state
from script import create_game_state


class StateControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = main_api.App()
        self.map1 = Map(2)
        self.state_ctrl = state_controller.StateController(self.app, self.app._display_surf)

    def test_change_state_1(self):
        self.assertIsInstance(self.state_ctrl.state, menu_state.Menu)
        self.state_ctrl.change_state("NONE")
        self.assertIsInstance(self.state_ctrl.state, menu_state.Menu)
        self.state_ctrl.change_state("PREV")
        self.assertIsNone(self.state_ctrl.state)
        self.state_ctrl.change_state("MENU")
        self.assertIsInstance(self.state_ctrl.state, menu_state.Menu)
        self.state_ctrl.change_state("CREATE")
        self.assertIsInstance(self.state_ctrl.state, create_game_state.CreateGame)
        self.state_ctrl.change_state("GAME")
        self.assertIsInstance(self.state_ctrl.state, game_state.Game)
        self.state_ctrl.change_state("PAUSE")
        self.assertIsInstance(self.state_ctrl.state, game_menu_state.GameMenu)
        self.state_ctrl.change_state("NONE")
        self.assertIsInstance(self.state_ctrl.state, game_menu_state.GameMenu)
        self.state_ctrl.change_state("PREV")
        self.assertIsInstance(self.state_ctrl.state, game_state.Game)

    def test_change_state_2(self):
        self.assertIsInstance(self.state_ctrl.state, menu_state.Menu)
        self.state_ctrl.change_state("NONE")
        self.assertIsInstance(self.state_ctrl.state, menu_state.Menu)
        self.state_ctrl.change_state("PREV")
        self.assertIsNone(self.state_ctrl.state)
        self.state_ctrl.change_state("MENU")
        self.assertIsInstance(self.state_ctrl.state, menu_state.Menu)
        self.state_ctrl.change_state("CREATE")
        self.assertIsInstance(self.state_ctrl.state, create_game_state.CreateGame)
        self.state_ctrl.change_state("GAME")
        self.assertIsInstance(self.state_ctrl.state, game_state.Game)
        self.state_ctrl.change_state("PAUSE")
        self.assertIsInstance(self.state_ctrl.state, game_menu_state.GameMenu)
        self.state_ctrl.change_state("NONE")
        self.assertIsInstance(self.state_ctrl.state, game_menu_state.GameMenu)
        self.state_ctrl.change_state("PREV")
        self.assertIsInstance(self.state_ctrl.state, game_state.Game)


suite = unittest.TestLoader().loadTestsFromTestCase(StateControllerTestCase)
print unittest.TextTestRunner(verbosity=3).run(suite)