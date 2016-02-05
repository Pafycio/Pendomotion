from tile import Tile

__author__ = 'pfert'


class StationTile(Tile):
    def __init__(self, tile_type, rotation=0, style=0):
        super(StationTile, self).__init__(tile_type, rotation, 2, 0, style)
