from script.map_src.map_loader import MapLoader
from script.map_src.control_map import ControlMap
import unittest
__author__ = 'pfert'


class NewMapStructureTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        loader = MapLoader(1)
        controlMap = ControlMap()
        controlMap.map = loader.get_map()
        controlMap.stations = loader.get_stations()
        self.assertEquals(len(controlMap.stations), 5)

suite = unittest.TestLoader().loadTestsFromTestCase(NewMapStructureTestCase)
print unittest.TextTestRunner(verbosity=3).run(suite)