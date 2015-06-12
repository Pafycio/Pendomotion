__author__ = 'Pawel'

import unittest
from script import images_flyweight as ic


class ImageControlTest(unittest.TestCase):
    def setUp(self):
        self.img = ic.ImagesFlyweight()

    def test_path_state_0(self):
        path_1 = self.img.get_image_by_id_state(0, 0)
        path_2 = self.img.get_image_by_id_state(0, 1)
        self.assertEqual(path_1, path_2)

    def test_path_state_1(self):
        path_1 = self.img.get_image_by_id_state(1, 0)
        path_2 = self.img.get_image_by_id_state(1, 0)
        self.assertEqual(path_1, path_2)

    def test_path_state_2(self):
        path_1 = self.img.get_image_by_id_state(2, 0)
        path_2 = self.img.get_image_by_id_state(2, 1)
        self.assertEqual(path_1, path_2)

    def test_path_state_3(self):
        path_1 = self.img.get_image_by_id_state(3, 0)
        path_2 = self.img.get_image_by_id_state(3, 1)
        self.assertNotEqual(path_1, path_2)

    def test_path_state_4(self):
        path_1 = self.img.get_image_by_id_state(4, 0)
        path_2 = self.img.get_image_by_id_state(4, 1)
        self.assertNotEqual(path_1, path_2)

    def test_path_state_5(self):
        path_1 = self.img.get_image_by_id_state(5, 0)
        path_2 = self.img.get_image_by_id_state(5, 1)
        self.assertNotEqual(path_1, path_2)

    def test_path_state_6(self):
        path_1 = self.img.get_image_by_id_state(9, 0)
        path_2 = self.img.get_image_by_id_state(9, 1)
        self.assertEqual(path_1, path_2)

    def test_path_state_7(self):
        path_1 = self.img.get_image_by_id_state(22, 0)
        path_2 = self.img.get_image_by_id_state(-1, 1)
        self.assertEqual(path_1, path_2)

    def test_path_state_8(self):
        path_1 = self.img.get_image_by_id_state(32, 0)
        path_2 = self.img.get_image_by_id_state(-22, 1)
        self.assertEqual(path_1, path_2)

suite = unittest.TestLoader().loadTestsFromTestCase(ImageControlTest)
print unittest.TextTestRunner(verbosity=3).run(suite)