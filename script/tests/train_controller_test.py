__author__ = 'Pawel'
# -*- coding: utf-8 -*-

import unittest
from script import map
from script import train_controller


class TrainControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.map = map.Map("2")
        self.map.load_map()
        self.t_control = train_controller.TrainController(self.map)

    def test_constructor_1(self):
        train_c = train_controller.TrainController(self.map)
        self.assertEqual(len(train_c.trains), 0)
        self.assertEqual(train_c.map, self.map)

    def test_add_train_1(self):
        self.t_control.add_train(0, 1, 0, 3)
        self.t_control.add_train(1, 2, -15, 3)
        self.t_control.add_train(2, 2, 334, -11)
        self.assertEqual(self.t_control.get_len(), 3)
        self.t_control.add_train(5, 2, 1030, 22)
        self.assertEqual(self.t_control.get_len(), 4)

    def test_add_train_2(self):
        self.t_control.add_train(0, 1, 0, 3)
        self.t_control.add_train(1, 2, -100, 3)
        self.t_control.add_train(2, -1, 20, 3)
        self.assertEqual(self.t_control.trains[2].finish, 0)
        self.assertEqual(self.t_control.get_len(), 3)
        self.t_control.add_train(8, 4, 100, 3)
        self.assertEqual(self.t_control.get_len(), 4)

    def test_rand_train_1(self):
        self.assertEqual(len(self.t_control.trains), 0)
        for i in xrange(0, 1000):
            self.t_control.rand_train()

        self.assertGreater(len(self.t_control.trains), 1)

    def test_rand_train_2(self):
        self.assertEqual(len(self.t_control.trains), 0)
        for i in xrange(0, 1000):
            self.t_control.rand_train()

        self.assertGreater(len(self.t_control.trains), 1)

    def test_collision_train_1(self):
        self.t_control.add_train(0, 1, 0, 3)
        self.t_control.add_train(0, 1, -15, 3)
        self.t_control.add_train(2, 2, 334, -11)
        self.assertEqual(self.t_control.get_len(), 3)
        self.t_control.add_train(1, 2, 1030, 22)
        self.assertEqual(self.t_control.get_len(), 4)
        self.t_control.check_collision()
        self.assertEqual(self.t_control.get_len(), 2)

    def test_collision_train_2(self):
        self.t_control.add_train(0, 1, 0, 3)
        self.t_control.add_train(0, 1, -15, 3)
        self.t_control.add_train(0, 1, 334, -11)
        self.assertEqual(self.t_control.get_len(), 3)
        self.t_control.add_train(1, 2, 1030, 22)
        self.assertEqual(self.t_control.get_len(), 4)
        self.t_control.check_collision()
        self.assertEqual(self.t_control.get_len(), 2)

    def test_add_value_1(self):
        self.assertEqual(self.t_control.map.map_score, 0, "Start with map score 0")
        self.t_control.add_value_to_score(50)
        self.assertEqual(self.t_control.map.map_score, 50)
        self.t_control.add_value_to_score(50)
        self.t_control.add_value_to_score(50)
        self.assertEqual(self.t_control.map.map_score, 150)
        self.t_control.add_value_to_score(-50)
        self.t_control.add_value_to_score(50)
        self.assertEqual(self.t_control.map.map_score, 150)
        self.t_control.add_value_to_score(-50)
        self.t_control.add_value_to_score(-25)
        self.assertEqual(self.t_control.map.map_score, 75)

    def test_check_move_1(self):
        self.t_control.add_train(0, 1, 100, 3)
        self.assertEqual(self.t_control.trains[0].can_move, False)
        self.assertEqual(self.t_control.trains[0].if_moving, False)
        self.assertEqual(self.t_control.trains[0].unblock, False)
        self.t_control.check_move(self.t_control[0])
        self.assertEqual(self.t_control.trains[0].can_move, True)
        self.assertEqual(self.t_control.trains[0].if_moving, True)
        self.assertEqual(self.t_control.trains[0].unblock, False)

    def test_check_move_2(self):
        self.t_control.add_train(1, 1, 100, 3)
        self.assertEqual(self.t_control.trains[0].can_move, False)
        self.assertEqual(self.t_control.trains[0].if_moving, False)
        self.assertEqual(self.t_control.trains[0].unblock, False)
        self.t_control.check_move(self.t_control[0])
        self.t_control.check_move(self.t_control[0])
        self.t_control.check_move(self.t_control[0])
        self.assertEqual(self.t_control.trains[0].can_move, True)
        self.assertEqual(self.t_control.trains[0].if_moving, True)
        self.assertEqual(self.t_control.trains[0].unblock, False)

    def test_train_enter_1(self):
        x, y = self.map.mechanic.get_center((0, 0))
        self.map.train_control.t_enter((x, y))
        self.assertEqual(self.map.mechanic.map_array[x][y].train_on, True)
        x, y = self.map.mechanic.get_center((1, 2))
        self.map.train_control.t_enter((x, y))
        self.assertEqual(self.map.mechanic.map_array[x][y].train_on, True)
        x, y = self.map.mechanic.get_center((3, 5))
        self.map.train_control.t_enter((x, y))
        self.assertEqual(self.map.mechanic.map_array[x][y].train_on, True)
        x, y = self.map.mechanic.get_center((0, 2))
        self.map.train_control.t_enter((x, y))
        self.assertEqual(self.map.mechanic.map_array[x][y].train_on, True)

    def test_train_enter_2(self):
        x, y = self.map.mechanic.get_center((0, 0))
        self.map.train_control.t_enter((x, y))
        self.assertEqual(self.map.mechanic.map_array[x][y].train_on, True)
        x, y = self.map.mechanic.get_center((1, 2))
        self.map.train_control.t_enter((x, y))
        self.assertEqual(self.map.mechanic.map_array[x][y].train_on, True)
        x, y = self.map.mechanic.get_center((3, 5))
        self.map.train_control.t_enter((x, y))
        self.assertEqual(self.map.mechanic.map_array[x][y].train_on, True)
        x, y = self.map.mechanic.get_center((0, 2))
        self.map.train_control.t_enter((x, y))
        self.assertEqual(self.map.mechanic.map_array[x][y].train_on, True)

        x, y = self.map.mechanic.get_center((0, 0))
        self.map.train_control.t_exit((x, y))
        self.assertEqual(self.map.mechanic.map_array[x][y].train_on, False)
        x, y = self.map.mechanic.get_center((1, 2))
        self.map.train_control.t_exit((x, y))
        self.assertEqual(self.map.mechanic.map_array[x][y].train_on, False)
        x, y = self.map.mechanic.get_center((3, 5))
        self.map.train_control.t_exit((x, y))
        self.assertEqual(self.map.mechanic.map_array[x][y].train_on, False)
        x, y = self.map.mechanic.get_center((0, 2))
        self.map.train_control.t_exit((x, y))
        self.assertEqual(self.map.mechanic.map_array[x][y].train_on, False)



suite = unittest.TestLoader().loadTestsFromTestCase(TrainControllerTestCase)
print unittest.TextTestRunner(verbosity=3).run(suite)