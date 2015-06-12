__author__ = 'Pawel'

import unittest
from script import images_flyweight as ic


class ImageControlTest(unittest.TestCase):
    def setUp(self):
        self.img_ctrl_0 = ic.ImagesFlyweight(0)
        self.img_ctrl_1 = ic.ImagesFlyweight(1)
        self.img_ctrl_2 = ic.ImagesFlyweight(2)
        self.img_ctrl_3 = ic.ImagesFlyweight(3)
        self.img_ctrl_4 = ic.ImagesFlyweight(4)
        self.img_ctrl_5 = ic.ImagesFlyweight(5)
        self.img_ctrl_9 = ic.ImagesFlyweight(9)
        self.img_ctrl_22 = ic.ImagesFlyweight(22)

    def test_path_state_0(self):
        path_1 = self.img_ctrl_0.get_by_state(0)
        path_2 = self.img_ctrl_0.get_by_state(1)
        self.assertNotEqual(path_1, path_2)
        self.assertTrue(path_1, r"images\blank.png")

    def test_path_state_1(self):
        path_1 = self.img_ctrl_1.get_by_state(0)
        path_2 = self.img_ctrl_1.get_by_state(1)
        self.assertNotEqual(path_1, path_2)

    def test_path_state_2(self):
        path_1 = self.img_ctrl_0.get_by_state(0)
        path_2 = self.img_ctrl_0.get_by_state(1)
        self.assertNotEqual(path_1, path_2)

    def test_list_paths_0(self):
        path_1 = self.img_ctrl_0.get_by_state(0)
        path_2 = self.img_ctrl_0.get_by_state(1)
        list = self.img_ctrl_0.get_image_list()
        self.assertTrue(list[0], path_1)
        self.assertTrue(list[1], path_2)

    def test_list_paths_1(self):
        path_1 = self.img_ctrl_9.get_by_state(0)
        path_2 = self.img_ctrl_9.get_by_state(1)
        list = self.img_ctrl_0.get_image_list()
        self.assertTrue(list[0], path_1)
        self.assertTrue(list[1], path_2)

    def test_list_paths_2(self):
        path_1 = self.img_ctrl_4.get_by_state(0)
        path_2 = self.img_ctrl_4.get_by_state(1)
        list = self.img_ctrl_0.get_image_list()
        self.assertTrue(list[0], path_1)
        self.assertTrue(list[1], path_2)

    def test_list_paths_3(self):
        path_1 = self.img_ctrl_22.get_by_state(0)
        path_2 = self.img_ctrl_22.get_by_state(1)
        self.assertEqual(path_1, path_2)
        list = self.img_ctrl_0.get_image_list()
        self.assertTrue(list[0], path_1)
        self.assertTrue(list[1], path_2)

    def test_get_image_out_of_state(self):
        path_1 = self.img_ctrl_4.get_by_state(4)
        path_2 = self.img_ctrl_4.get_by_state(7)
        self.assertEqual(path_1, path_2)

suite = unittest.TestLoader().loadTestsFromTestCase(ImageControlTest)
print unittest.TextTestRunner(verbosity=3).run(suite)