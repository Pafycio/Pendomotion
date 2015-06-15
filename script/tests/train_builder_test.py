__author__ = 'Pawel'
# -*- coding: utf-8 -*-

import unittest
from script import train_builder
from script import map_part


class TrainBuilderTestCase(unittest.TestCase):
    def setUp(self):
        self.builder = train_builder.TrainBuilder()
        self.station_1 = map_part.Part(9, 0, 2, 2)
        self.station_2 = map_part.Part(9, 2, 4, 6)

    def test_set_station_1(self):
        self.builder.set_start_station(self.station_1)
        self.assertEqual(self.builder.start, self.station_1)
        self.assertEqual(self.builder.direction, self.station_1.rotation)
        self.assertEqual(self.builder.pos_x, self.station_1.x)
        self.assertEqual(self.builder.pos_y, self.station_1.y)

    def test_set_finish_station_1(self):
        self.builder.set_finish_station(5)
        self.assertEqual(self.builder.finish, 5)

    def test_set_speed_1(self):
        self.builder.set_speed(5)
        self.assertEqual(self.builder.speed, 5)
        self.builder.set_speed(-3)
        self.assertEqual(self.builder.speed, 0)

    def test_set_speed_2(self):
        self.builder.set_value(222)
        self.assertEqual(self.builder.value, 222)
        self.builder.set_value(-3)
        self.assertEqual(self.builder.value, 0)

    def test_set_bool_values_1(self):
        self.builder.set_bool_values(True, True, True)
        self.assertEqual(self.builder.can_move, True)
        self.assertEqual(self.builder.if_moving, True)
        self.assertEqual(self.builder.unblock, True)

        self.builder.set_bool_values(True, False, True)
        self.assertEqual(self.builder.can_move, False)
        self.assertEqual(self.builder.if_moving, True)
        self.assertEqual(self.builder.unblock, True)

    def test_set_animation(self):
        self.builder.set_animation(322)
        self.assertEqual(self.builder.animation, 322)

        self.builder.set_animation(0)
        self.assertEqual(self.builder.animation, 0)

    def test_set_time(self):
        self.builder.set_time(322)
        self.assertEqual(self.builder.time, 322)

        self.builder.set_time(32)
        self.assertNotEqual(self.builder.time, 0)

    def test_create_train_1(self):
        self.builder.set_start_station(self.station_1)
        self.builder.set_finish_station(3)
        self.builder.set_bool_values(False, False, False)
        self.builder.set_value(325)
        self.builder.set_speed(3)
        self.builder.set_animation(0)
        self.builder.set_time(20)
        new_train = self.builder.create_train()

        self.assertEqual(new_train.finish, 3)
        self.assertEqual(new_train.animation, 0)
        self.assertEqual(new_train.x, 2)
        self.assertEqual(new_train.y, 2)
        self.assertEqual(new_train.speed, 3)
        self.assertEqual(new_train.if_moving, False)
        self.assertEqual(new_train.can_move, False)
        self.assertEqual(new_train.unblock, False)

    def test_create_train_2(self):
        self.builder.set_start_station(self.station_2)
        self.builder.set_finish_station(2)
        self.builder.set_bool_values(False, True, True)
        self.builder.set_value(111)
        self.builder.set_speed(-3)
        self.builder.set_animation(22)
        self.builder.set_time(0)
        new_train = self.builder.create_train()

        self.assertEqual(new_train.finish, 2)
        self.assertEqual(new_train.animation, 22)
        self.assertEqual(new_train.x, 4)
        self.assertEqual(new_train.y, 6)
        self.assertEqual(new_train.speed, 0)
        self.assertEqual(new_train.if_moving, False)
        self.assertEqual(new_train.can_move, True)
        self.assertEqual(new_train.unblock, True)

suite = unittest.TestLoader().loadTestsFromTestCase(TrainBuilderTestCase)
print unittest.TextTestRunner(verbosity=3).run(suite)