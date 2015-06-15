__author__ = 'Pawel'
# -*- coding: utf-8 -*-

import unittest
from script import map_part
from script import images_flyweight


class PartTestCase(unittest.TestCase):
    def setUp(self):
        self.part_1 = map_part.Part(1, 3)
        self.part_2 = map_part.Part(4, 2)
        self.img_f = images_flyweight.ImagesFlyweight()

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
        self.part_1.train_enter()
        self.part_1.change_state()
        self.assertEquals(self.part_1.state, 0)

    def test_state_true_2(self):
        self.part_2.state = 0
        self.part_2.change_state()
        self.assertEquals(self.part_2.state, 1)
        self.part_2.change_state()
        self.assertEquals(self.part_2.state, 0)
        self.part_2.train_enter()
        self.part_2.change_state()
        self.assertEquals(self.part_2.state, 0)

    def test_get_image_1(self):
        path1 = self.img_f.get_image_by_id_state(4, 1)

        path2 = self.img_f.get_image_by_id_state(4, 2)
        self.assertNotEqual(path1, path2)
        path1 = self.img_f.get_image_by_id_state(2, 1)

        path2 = self.img_f.get_image_by_id_state(2, 2)
        self.assertEqual(path1, path2)
        path1 = self.img_f.get_image_by_id_state(9, 1)

        path2 = self.img_f.get_image_by_id_state(9, 2)
        self.assertEqual(path1, path2)
        path1 = self.img_f.get_image_by_id_state(1, 1)

        path2 = self.img_f.get_image_by_id_state(1, 2)
        self.assertEqual(path1, path2)



suite = unittest.TestLoader().loadTestsFromTestCase(PartTestCase)
print unittest.TextTestRunner(verbosity=3).run(suite)