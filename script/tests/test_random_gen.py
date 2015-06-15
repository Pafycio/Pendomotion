__author__ = 'Pawel'

import unittest
from script import state
from script import main_api


class StateTestCase(unittest.TestCase):
    def setUp(self):
        self.app = main_api.App()
        self.state = state.State(self.app._display_surf, None)

    def test_1(self):
        self.assertEqual(self.state.get_prev(), None)
        self.assertEqual(self.state.surf, self.app._display_surf)
        self.state.on_render()
        self.assertEqual(self.state.get_prev(), None)
        self.assertEqual(self.state.surf, self.app._display_surf)

suite = unittest.TestLoader().loadTestsFromTestCase(StateTestCase)
print unittest.TextTestRunner(verbosity=3).run(suite)