__author__ = 'Pawel'
from map_part import Part
from map_mechanic import MapMechanic
from train_controller import TrainController

from pygame import image as img
from pygame import transform as trans
from random import randint


class Map(object):
    """
    Map Class
    """
    def __init__(self, level_id):
        """
        :param level_id:
        :return:
        """
        self.level_id = level_id
        self.mechanic = None
        self.train_control = None
        self.trains = []
        self.stations = []
        self.x = 0
        self.y = 0
        self.map_score = 0
        self.crash = 0

    def load_map(self):
        """
        Load map from file
        Create Map Mechanic
        Create list of stations
        :return:
        """
        level_file = open('maps/level_'+self.level_id, "r")
        xy = level_file.readline().split()
        self.x = int(xy[1])
        self.y = int(xy[0])
        print "Load map size "+str(self.x) + " " + str(self.y)
        map_parts = [i.rstrip(r"\n*") for i in level_file]
        self.mechanic = MapMechanic((self.x, self.y))
        self.train_control = TrainController(self.stations, self.mechanic, self)
        k = 0
        for j in xrange(self.x):
            for i in xrange(self.y):
                cur_part = map_parts[k].split()
                t_b = int(cur_part[0])
                rot = int(cur_part[1])
                new_part = Part(t_b, rot, i, j)
                self.mechanic.add_at((i, j), new_part)
                if new_part.id == 9:
                    self.add_station(new_part)
                k += 1

    def print_mechanic(self):
        """
        Print Mechanic array
        :return:
        """
        for i in xrange(self.mechanic.x):
            for j in xrange(self.mechanic.y):
                print str(self.mechanic.map_array[j][i])+"",
            print

    def part_on_click(self, (x, y)):
        """
        Cound i, j
        Run metode on Part change_state((i, j))
        :return:
        """
        if x >= 640 or y >= 512:
            pass
        else:
            i = 0
            j = 0
            x -= 64
            while x > 0:
                i += 1
                x -= 64
            y -= 64
            while y > 0:
                j += 1
                y -= 64
            #print "Main array x:"+str(i) + " y:" + str(j)
            self.mechanic.change_state((i, j))

        #  print "Mechanic array:"+str(self.mechanic.get_center((i, j)))

    def get_image(self, (x, y)):
        """
        Get image with set rotation
        :return:
        """
        (x, y) = self.mechanic.get_center((x, y))
        path = self.mechanic.map_array[x][y].get_image_path()
        image = img.load(path).convert_alpha()
        image = trans.rotate(image, self.mechanic.map_array[x][y].rotation * (-90))
        return image

    def get_id(self, (x, y)):
        """
        Get block type on x,y
        :return:
        """
        (x, y) = self.mechanic.get_center((x, y))
        return self.mechanic.map_array[x][y].id

    def get_station_num(self, (x, y)):
        """
        Set station number on x,y
        :return:
        """
        (x, y) = self.mechanic.get_center((x, y))
        return self.mechanic.map_array[x][y].station_num

    def add_station(self, part):
        """
        Add station to List
        :param part:
        :return:
        """
        part.station_num = int(len(self.stations))
        self.stations.append(part)
