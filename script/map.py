__author__ = 'Pawel'
from map_part import Part
from map_mechanic import MapMechanic

from train import Train
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

    def rand_train(self):
        """
        Random generating trains with rand start and rand end
        :return:
        """
        start_statnion = randint(0, len(self.stations)-1)
        finish_statnion = randint(0, len(self.stations)-1)
        value = 100
        gen_new = randint(0, 10000)
        if len(self.trains) == 0:
            self.add_train(start_statnion, finish_statnion, value)
        elif len(self.trains) == 1 and gen_new <= 100:
            self.add_train(start_statnion, finish_statnion, value)
        elif len(self.trains) == 2 and gen_new <= 10:
            self.add_train(start_statnion, finish_statnion, value)

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

    def add_train(self, start, finish, value):
        """
        Add train to List
        :param start:
        :param finish:
        :param value:
        :return:
        """
        self.trains.append(Train(self.stations[start], finish, value))

    def delete_train(self, train):
        """
        Delete train from List
        :param train:
        :return:
        """
        self.trains.remove(train)

    def t_enter(self, (x, y)):
        """
        Train enter on part x,y
        :return:
        """
        self.mechanic.map_array[x][y].train_enter()

    def t_exit(self, (x, y)):
        """
        Train exit from part x,y
        :return:
        """
        self.mechanic.map_array[x][y].train_exit()

    def check_collision(self):
        """
        Iterate on trains List and check collision
        :return:
        """
        for i in self.trains:
            for j in self.trains:
                if i != j and i.x == j.x and i.y == j.y:
                    self.delete_train(i)
                    self.delete_train(j)

    def move_to_pos(self, train, (x, y), direction=0):
        """
        Move train to position x,y and change direction
        :param train:
        :param direction:
        :return:
        """
        train.if_moving = True
        train.set_pos(x, y)
        train.change_direction(direction)

    def move_trains(self):
        """
        Check posibillities and move all trains forward
        :return:
        """
        for i in self.trains:
            if not i.if_moving:
                curr = i
                curr.can_move = True
                cx, cy = curr.get_pos()
                old_x, old_y = self.mechanic.get_center((cx, cy))
                if curr.direction == 0:
                    x, y = self.mechanic.get_center((cx, cy-1))
                    if self.mechanic.map_array[x][y+1] == "_"and not self.mechanic.map_array[x][y].id == 9:
                        curr.if_moving = False
                        curr.can_move = False
                    elif self.mechanic.map_array[x][y+1] == 1 and self.mechanic.map_array[x][y-1] == 1:  # prosto
                        self.t_exit((old_x, old_y))
                        self.move_to_pos(curr, (cx, cy-1))
                        self.t_enter((x, y))
                    elif self.mechanic.map_array[x][y+1] == 1 and self.mechanic.map_array[x+1][y] == 1:  # w prawio
                        self.t_exit((old_x, old_y))
                        self.move_to_pos(curr, (cx, cy-1), 1)
                        self.t_enter((x, y))
                    elif self.mechanic.map_array[x][y+1] == 1 and self.mechanic.map_array[x-1][y] == 1:  # w lewo
                        self.t_exit((old_x, old_y))
                        self.move_to_pos(curr, (cx, cy-1), -1)
                        self.t_enter((x, y))
                    elif self.mechanic.map_array[x][y].id == 9:
                        if self.mechanic.map_array[x][y].station_num == curr.finish:
                            self.t_exit((old_x, old_y))
                            self.move_to_pos(curr, (cx, cy-1))
                            self.t_enter((x, y))
                            self.map_score += curr.get_value()
                            self.delete_train(curr)
                            self.t_exit((x, y))
                            #print "Jeste w domku"

                        else:
                            self.move_to_pos(curr, (cx, cy-1), 2)
                    else:
                        print "test"
                        curr.if_moving = False
                        curr.can_move = False

                elif curr.direction == 1:
                    x, y = self.mechanic.get_center((cx+1, cy))
                    if self.mechanic.map_array[x-1][y] == "_"and not self.mechanic.map_array[x][y].id == 9:
                        curr.if_moving = False
                        curr.can_move = False
                    elif self.mechanic.map_array[x-1][y] == 1 and self.mechanic.map_array[x+1][y] == 1:  # prosto
                        self.t_exit((old_x, old_y))
                        self.move_to_pos(curr, (cx+1, cy))
                        self.t_enter((x, y))
                    elif self.mechanic.map_array[x-1][y] == 1 and self.mechanic.map_array[x][y+1] == 1:  # w prawio
                        self.t_exit((old_x, old_y))
                        self.move_to_pos(curr, (cx+1, cy), 1)
                        self.t_enter((x, y))
                    elif self.mechanic.map_array[x-1][y] == 1 and self.mechanic.map_array[x][y-1] == 1:  # w lewo
                        self.t_exit((old_x, old_y))
                        self.move_to_pos(curr, (cx+1, cy), -1)
                        self.t_enter((x, y))
                    elif self.mechanic.map_array[x][y].id == 9:
                        if self.mechanic.map_array[x][y].station_num == curr.finish:
                            self.t_exit((old_x, old_y))
                            self.move_to_pos(curr, (cx+1, cy))
                            self.t_enter((x, y))
                            self.map_score += curr.get_value()
                            self.delete_train(curr)
                            self.t_exit((x, y))
                            #print "Jeste w domku"
                        else:
                            self.move_to_pos(curr, (cx+1, cy), 2)
                    else:
                        print "test"
                        curr.if_moving = False
                        curr.can_move = False

                elif curr.direction == 2:
                    x, y = self.mechanic.get_center((cx, cy+1))
                    if self.mechanic.map_array[x][y-1] == "_" and not self.mechanic.map_array[x][y].id == 9:
                        curr.if_moving = False
                        curr.can_move = False
                    elif self.mechanic.map_array[x][y-1] == 1 and self.mechanic.map_array[x][y+1] == 1:  # prosto
                        self.t_exit((old_x, old_y))
                        self.move_to_pos(curr, (cx, cy+1))
                        self.t_enter((x, y))
                    elif self.mechanic.map_array[x][y-1] == 1 and self.mechanic.map_array[x-1][y] == 1:  # w prawio
                        self.t_exit((old_x, old_y))
                        self.move_to_pos(curr, (cx, cy+1), 1)
                        self.t_enter((x, y))
                    elif self.mechanic.map_array[x][y-1] == 1 and self.mechanic.map_array[x+1][y] == 1:  # w lewo
                        self.t_exit((old_x, old_y))
                        self.move_to_pos(curr, (cx, cy+1), -1)
                        self.t_enter((x, y))
                    elif self.mechanic.map_array[x][y].id == 9:
                        if self.mechanic.map_array[x][y].station_num == curr.finish:
                            self.t_exit((old_x, old_y))
                            self.move_to_pos(curr, (cx, cy+1))
                            self.t_enter((x, y))
                            self.map_score += curr.get_value()
                            self.delete_train(curr)
                            self.t_exit((x, y))
                            #print "Jeste w domku"
                        else:
                            self.move_to_pos(curr, (cx, cy+1), 2)

                    else:
                        print "test"
                        curr.if_moving = False
                        curr.can_move = False

                elif curr.direction == 3:
                    x, y = self.mechanic.get_center((cx-1, cy))
                    if self.mechanic.map_array[x+1][y] == "_"and not self.mechanic.map_array[x][y].id == 9:
                        curr.if_moving = False
                        curr.can_move = False
                    elif self.mechanic.map_array[x+1][y] == 1 and self.mechanic.map_array[x-1][y] == 1:  # prosto
                        self.t_exit((old_x, old_y))
                        self.move_to_pos(curr, (cx-1, cy))
                        self.t_enter((x, y))
                    elif self.mechanic.map_array[x+1][y] == 1 and self.mechanic.map_array[x][y-1] == 1:  # w prawio
                        self.t_exit((old_x, old_y))
                        self.move_to_pos(curr, (cx-1, cy), 1)
                        self.t_enter((x, y))
                    elif self.mechanic.map_array[x+1][y] == 1 and self.mechanic.map_array[x][y+1] == 1:  # w lewo
                        self.t_exit((old_x, old_y))
                        self.move_to_pos(curr, (cx-1, cy), -1)
                        self.t_enter((x, y))
                    elif self.mechanic.map_array[x][y].id == 9:
                        if self.mechanic.map_array[x][y].station_num == curr.finish:
                            self.t_exit((old_x, old_y))
                            self.move_to_pos(curr, (cx-1, cy))
                            self.t_enter((x, y))
                            self.map_score += curr.get_value()
                            self.delete_train(curr)
                            self.t_exit((x, y))
                            #print "Jeste w domku"
                        else:
                            self.move_to_pos(curr, (cx-1, cy), 2)

                    else:
                        print "test"
                        curr.if_moving = False
                        curr.can_move = False
                self.check_collision()
