from tile import Tile
import random

__author__ = 'pfert'


class SteerTile(Tile):
    def __init__(self, tile_type, rotation=0, style=0):
        super(SteerTile, self).__init__(tile_type, rotation, 2, 0, style)
        self.state = random.randint(0, 1)


