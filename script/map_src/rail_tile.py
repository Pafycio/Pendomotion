from tile import Tile

__author__ = 'pfert'


class RailTile(Tile):
    def __init__(self, tile_type, rotation=0, style=0):
        super(RailTile, self).__init__(tile_type, rotation, 1, 0, style)


