__author__ = 'Pawel'
# -*- coding: utf-8 -*-

import unittest
from script import map_part


class PartTestCase(unittest.TestCase):
    def setUp(self):
        self.part_1 = map_part.Part(1, 3)
        self.part_2 = map_part.Part(4, 2)

    def test_rotate(self):
        self.part_1.rotate()
        self.assertEquals(self.part_1.rotation, 0)
        self.part_1.rotate(2)
        self.part_1.rotate()
        self.assertEquals(self.part_1.rotation, 3)
        self.part_1.rotate(-2)
        self.assertEquals(self.part_1.rotation, 1)

    def test_state_true(self):
        self.part_1.change_state()
        self.assertEquals(self.part_1.state, 0)
        self.part_1.change_state()
        self.assertEquals(self.part_1.state, 0)
        self.part_1.train_on = True
        self.part_1.change_state()
        self.assertEquals(self.part_1.state, 0)

    def test_state_true_2(self):
        self.part_2.change_state()
        self.assertEquals(self.part_2.state, 1)
        self.part_2.change_state()
        self.assertEquals(self.part_2.state, 0)
        self.part_2.train_on = True
        self.part_2.change_state()
        self.assertEquals(self.part_2.state, 0)

suite = unittest.TestLoader().loadTestsFromTestCase(PartTestCase)
print unittest.TextTestRunner(verbosity=3).run(suite)