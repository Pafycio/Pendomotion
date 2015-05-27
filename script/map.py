__author__ = 'Pawel'
from map_part import Part
from map_mechanic import MapMechanic

from train import Train
from pygame import image as img
from pygame import transform as trans


class Map(object):
    def __init__(self, l_id):
        self.level_id = l_id
        self.mechanic = None
        self.trains = []
        self.stations = []
        #self.map_array = None
        self.x = 0
        self.y = 0

    def load_map(self):
        level_file = open('maps/level_'+self.level_id, "r")
        xy = level_file.readline().split()
        self.x = int(xy[1])
        self.y = int(xy[0])
        print "Load map size "+str(self.x) + " " + str(self.y)
        map_parts = [i.rstrip(r"\n*") for i in level_file]
        #self.map_array = [[Part(0, 0) for i in xrange(self.x)] for j in xrange(self.y)]
        self.mechanic = MapMechanic((self.x, self.y))
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

                #state = self.map_array[i][j].state
                k += 1

        self.add_train(0)
        self.add_train(1)

    def print_mechanic(self):
        for i in xrange(self.mechanic.x):
            for j in xrange(self.mechanic.y):
                print str(self.mechanic.map_array[j][i])+"",
            print

    def part_on_click(self, (x, y)):
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
        (x, y) = self.mechanic.get_center((x, y))
        path = self.mechanic.map_array[x][y].get_image_path()
        image = img.load(path).convert_alpha()
        image = trans.rotate(image, self.mechanic.map_array[x][y].rotation * (-90))
        return image

    def add_station(self, part):
        self.stations.append(part)

    def add_train(self, station_num=0):
        self.trains.append(Train("A", 100, self.stations[station_num]))

    def move_trains(self):
        for i in self.trains:
            curr = i
            cx, cy = curr.get_pos()

            if curr.direction == 0:
                x, y = self.mechanic.get_center((cx, cy-1))
                if self.mechanic.map_array[x][y+1] == 1 and self.mechanic.map_array[x][y-1] == 1:  # prosto
                    curr.set_pos(cx, cy-1)
                elif self.mechanic.map_array[x][y+1] == 1 and self.mechanic.map_array[x+1][y] == 1:  # w prawio
                    curr.set_pos(cx, cy-1)
                    curr.change_direction(1)
                elif self.mechanic.map_array[x][y+1] == 1 and self.mechanic.map_array[x-1][y] == 1:  # w lewo
                    curr.set_pos(cx, cy-1)
                    curr.change_direction(-1)
                elif self.mechanic.map_array[x][y].id == 9:
                    curr.set_pos(cx, cy-1)
                    curr.change_direction(2)
                else:
                    #print "MH ?! 0"
                    pass

            elif curr.direction == 1:
                x, y = self.mechanic.get_center((cx+1, cy))
                if self.mechanic.map_array[x-1][y] == 1 and self.mechanic.map_array[x+1][y] == 1:  # prosto
                    curr.set_pos(cx+1, cy)
                elif self.mechanic.map_array[x-1][y] == 1 and self.mechanic.map_array[x][y+1] == 1:  # w prawio
                    curr.set_pos(cx+1, cy)
                    curr.change_direction(1)
                elif self.mechanic.map_array[x-1][y] == 1 and self.mechanic.map_array[x][y-1] == 1:  # w lewo
                    curr.set_pos(cx+1, cy)
                    curr.change_direction(-1)
                elif self.mechanic.map_array[x][y].id == 9:
                    curr.set_pos(cx+1, cy)
                    curr.change_direction(2)
                else:
                    #print "MH ?! 1"
                    pass

            elif curr.direction == 2:
                x, y = self.mechanic.get_center((cx, cy+1))
                print x
                print y
                if self.mechanic.map_array[x][y-1] == 1 and self.mechanic.map_array[x][y+1] == 1:  # prosto
                    curr.set_pos(cx, cy+1)
                elif self.mechanic.map_array[x][y-1] == 1 and self.mechanic.map_array[x-1][y] == 1:  # w prawio
                    curr.set_pos(cx, cy+1)
                    curr.change_direction(1)
                elif self.mechanic.map_array[x][y-1] == 1 and self.mechanic.map_array[x+1][y] == 1:  # w lewo
                    curr.set_pos(cx, cy+1)
                    curr.change_direction(-1)
                elif self.mechanic.map_array[x][y].id == 9:
                    curr.set_pos(cx, cy+1)
                    curr.change_direction(2)
                else:
                    #print "HM ?! 2"
                    pass

            elif curr.direction == 3:
                x, y = self.mechanic.get_center((cx-1, cy))
                if self.mechanic.map_array[x+1][y] == 1 and self.mechanic.map_array[x-1][y] == 1:  # prosto
                    curr.set_pos(cx-1, cy)
                elif self.mechanic.map_array[x+1][y] == 1 and self.mechanic.map_array[x][y-1] == 1:  # w prawio
                    curr.set_pos(cx-1, cy)
                    curr.change_direction(1)
                elif self.mechanic.map_array[x+1][y] == 1 and self.mechanic.map_array[x][y+1] == 1:  # w lewo
                    curr.set_pos(cx-1, cy)
                    curr.change_direction(-1)
                elif self.mechanic.map_array[x][y].id == 9:
                    curr.set_pos(cx-1, cy)
                    curr.change_direction(2)
                else:
                    #print "MH ?! 3"
                    pass
