from rail_tile import RailTile
from blank_tile import BlankTile
from station_tile import StationTile
from steer_tile import SteerTile

__author__ = 'pfert'


def get_tile_type(tile_type):
    return {
        0: 'Blank',
        1: 'Straight',
        2: 'Curve',
        3: 'StraightRight',
        4: 'StraightLeft',
        5: 'Cross',
        9: 'Station',
    }.get(tile_type, 'Blank')


class MapLoader(object):
    def __init__(self, map_id):
        level_file = open('maps/level_' + str(map_id), "r")
        xy = level_file.readline().split()
        self.x = int(xy[1])
        self.y = int(xy[0])
        style = 0
        map_parts = [i.rstrip(r"\n*") for i in level_file]

        self.map_array = [[None for i in xrange(self.x)] for j in xrange(self.y)]
        self.stations = []
        k = 0
        for j in xrange(self.x):
            for i in xrange(self.y):
                cur_part = map_parts[k].split()
                tile_type = get_tile_type(int(cur_part[0]))
                rot = int(cur_part[1])
                if tile_type == 'Straight':
                    new_part = RailTile(tile_type, rot, style)
                elif tile_type == 'Curve':
                    new_part = RailTile(tile_type, rot, style)
                elif tile_type == 'StraightRight':
                    new_part = SteerTile(tile_type, rot, style)
                elif tile_type == 'StraightLeft':
                    new_part = SteerTile(tile_type, rot, style)
                elif tile_type == 'Cross':
                    new_part = SteerTile(tile_type, rot, style)
                elif tile_type == 'Station':
                    new_part = StationTile(tile_type + "_" + str(len(self.stations)), rot)
                    self.stations.append(new_part)
                else:
                    new_part = BlankTile(tile_type, rot)

                self.map_array[i][j] = new_part
                k += 1

    def add_station(self, station):
        self.stations.append(station)

    def get_stations(self):
        return self.stations

    def get_map(self):
        return self.map_array

    def get_map_size(self):
        return self.x, self.y