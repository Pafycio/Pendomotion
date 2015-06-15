__author__ = 'Pawel'
# -*- coding: utf-8 -*-

import unittest
from script import train


class TrainTestCase(unittest.TestCase):
    def setUp(self):
        self.train_1 = train.Train(3, 1, 0, False, False, False,
                                   0, 100, 2, 2, 15, 6)

        self.train_2 = train.Train(4, 2, 0, True, False, False,
                                   3, 100, 4, 3, 60, 10)

    def test_change_direction_1(self):
        self.assertEqual(self.train_1.direction, 0)
        self.assertEqual(self.train_2.direction, 3)
        self.train_1.change_direction(2)
        self.train_2.change_direction(1)
        self.assertEqual(self.train_1.direction, 2)
        self.assertEqual(self.train_2.direction, 0)

    def test_change_direction_2(self):
        self.assertEqual(self.train_1.direction, 0)
        self.assertEqual(self.train_2.direction, 3)
        self.train_1.change_direction(-1)
        self.train_2.change_direction(-3)
        self.assertEqual(self.train_1.direction, 3)
        self.assertEqual(self.train_2.direction, 0)

    def test_change_direction_3(self):
        self.assertNotEqual(self.train_1.direction, 2)
        self.assertNotEqual(self.train_2.direction, 0)
        self.train_1.change_direction(2)
        self.train_2.change_direction(0)
        self.assertNotEqual(self.train_1.direction, 1)
        self.assertNotEqual(self.train_2.direction, 1)

    def test_time_to_start_1(self):
        for i in xrange(0, 5):
            self.assertEqual(self.train_1.time_to_start(), False)
            self.assertEqual(self.train_1.unblock, False)
        self.assertEqual(self.train_1.time_to_start(), True)
        self.assertEqual(self.train_1.unblock, True)
        self.train_1.time = 5
        self.assertEqual(self.train_1.unblock, True)
        self.train_1.time_to_start()
        self.assertEqual(self.train_1.unblock, False)
        self.assertEqual(self.train_1.time, 4)

    def test_time_to_start_2(self):
        for i in xrange(0, 9):
            self.assertEqual(self.train_2.time_to_start(), False)
            self.assertEqual(self.train_2.unblock, False)
        self.assertEqual(self.train_2.time_to_start(), True)
        self.assertEqual(self.train_2.unblock, True)
        self.train_2.time = 5
        self.assertEqual(self.train_2.unblock, True)
        self.train_2.time_to_start()
        self.assertEqual(self.train_2.unblock, False)
        self.assertEqual(self.train_2.time, 4)

    def test_time_to_start_3(self):
        self.train_1.time = -10
        self.assertEqual(self.train_1.time_to_start(), True)

    def test_set_value_1(self):
        self.train_1.set_value(15)
        self.assertEqual(self.train_1.get_value(), 15)
        self.train_1.set_value(0)
        self.assertEqual(self.train_1.get_value(), 0)
        self.train_1.set_value(-15)
        self.assertEqual(self.train_1.get_value(), 0)
        self.train_1.set_value(1)
        self.assertEqual(self.train_1.get_value(), 1)

    def test_set_speed_1(self):
        self.train_1.set_speed(22)
        self.assertEqual(self.train_1.get_speed(), 22)
        self.train_1.set_speed(0)
        self.assertEqual(self.train_1.get_speed(), 0)
        self.train_1.set_speed(-15)
        self.assertEqual(self.train_1.get_speed(), 0)
        self.train_1.set_speed(1)
        self.assertEqual(self.train_1.get_speed(), 1)

    def test_animation_step_1(self):
        self.train_1.animation = 15
        self.train_1.animation_step(3)
        self.assertEqual(self.train_1.animation, 15)
        #  can move = False
        self.train_1.can_move = True
        self.train_1.animation_step(3)
        self.assertEqual(self.train_1.animation, 18)
        self.train_1.animation_step(-15)
        self.assertEqual(self.train_1.animation, 18)
        self.train_1.animation_step(2)
        self.assertEqual(self.train_1.animation, 20)
        self.train_1.animation_step(33)
        self.assertEqual(self.train_1.animation, 53)

    def test_animation_step_2(self):
        self.train_2.can_move = True
        self.train_2.animation_step(4)
        self.assertEqual(self.train_2.if_moving, False)
        self.train_2.animation_step(0)
        self.assertEqual(self.train_2.animation, 0)
        self.train_2.animation_step(2)
        self.assertEqual(self.train_2.animation, 2)
        self.train_2.animation_step(-33)
        self.assertEqual(self.train_2.animation, 2)

    def test_set_pos_1(self):
        self.train_1.set_pos(5, 11)
        self.assertEqual(self.train_1.x, 5)
        self.assertEqual(self.train_1.y, 11)
        self.train_1.set_pos(0, 0)
        self.assertEqual(self.train_1.x, 0)
        self.assertEqual(self.train_1.y, 0)

    def test_set_strategy_1(self):
        self.train_1.set_strategy(True, True)
        self.assertEqual(self.train_1.can_move, True)
        self.assertEqual(self.train_1.if_moving, True)
        self.train_2.set_strategy(True, False)
        self.assertEqual(self.train_2.can_move, True)
        self.assertEqual(self.train_2.if_moving, False)

suite = unittest.TestLoader().loadTestsFromTestCase(TrainTestCase)
print unittest.TextTestRunner(verbosity=3).run(suite)