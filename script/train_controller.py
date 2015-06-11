__author__ = 'Pawel'

from random import randint
from train_builder import TrainBuilder


class TrainController(object):
    def __init__(self, stations, mechanic, map):
        """
        :param stations:
        :return:
        """
        self.trains = []
        self.stations = stations
        self.mechanic = mechanic
        self.train_build = TrainBuilder()
        self.map = map

    def __delattr__(self, item):
        """
        :param item:
        :return:
        """
        self.trains.remove(item)

    def __str__(self):
        """
        :return:
        """
        return "Trains "+str(len(self.trains))

    def __getitem__(self, item):
        """
        :param item:
        :return:
        """
        return self.trains[item]

    def on_loop(self):
        self.rand_train()
        self.move_trains()

    def get_len(self):
        """
        :return:
        """
        return len(self.trains)

    def add_train(self, start, finish, value, speed):
        """
        Add train to List
        :param start:
        :param finish:
        :param value:
        :return:
        """
        self.train_build.set_start_station(self.stations[start])
        self.train_build.set_finish_station(finish)
        self.train_build.set_bool_values(False, False, False)
        self.train_build.set_value(value)
        self.train_build.set_speed(speed)
        self.train_build.set_animation(0)
        self.train_build.set_time(20)
        self.trains.append(self.train_build.create_train())

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
            self.add_train(start_statnion, finish_statnion, value, 3)
        elif len(self.trains) == 1 and gen_new <= 100:
            self.add_train(start_statnion, finish_statnion, value, 3)
        elif len(self.trains) == 2 and gen_new <= 10:
            self.add_train(start_statnion, finish_statnion, value, 3)

    def check_collision(self):
        """
        Iterate on trains List and check collision
        :return:
        """
        for i in self.trains:
            for j in self.trains:
                if i != j and i.x == j.x and i.y == j.y:
                    self.trains.remove(i)
                    self.trains.remove(j)

    def add_value_to_score(self, value):
        self.map.map_score += value

    def move_to(self, train, (x, y), direction=0, can_move=True):
        """
        Move train to position x,y and change direction
        :param train:
        :param direction:
        :return:
        """
        train.if_moving = True
        train.can_move = can_move
        train.set_pos(x, y)
        train.change_direction(direction)

    def set_strategy(self, train):
        if train.time_to_start():
            if not train.can_move and not train.if_moving:
                self.check_move(train)
            elif train.can_move and not train.if_moving:
                self.check_move(train)
            if train.can_move and train.if_moving:
                train.animation_step(2)
            elif not train.can_move and train.if_moving:
                train.animation_step(0)

    def move_trains(self):
        """
        Check posibillities and move all trains forward
        :return:
        """
        for i in self.trains:
            self.set_strategy(i)

    def check_move(self, train):
        """

        :param train:
        :return:
        """
        cx, cy = train.get_pos()
        old_x, old_y = self.mechanic.get_center((cx, cy))
        if train.unblock:
            #print "Wystartowalen "+str(cx)+" "+str(cy)
            self.move_to(train, (cx, cy))
            train.unblock = False
        elif train.direction == 0:
            x, y = self.mechanic.get_center((cx, cy-1))
            if self.mechanic.map_array[x][y+1] == "_" and not self.mechanic.map_array[x][y].id == 9:
                train.if_moving = False
                train.can_move = False
                train.time = 20 #czas przed ponownym ruszeniem
                self.move_to(train, (cx, cy))
                #print "Nie moge jechac a jade"
            elif self.mechanic.map_array[x][y+1] == 1 and self.mechanic.map_array[x][y-1] == 1:  # prosto
                self.t_exit((old_x, old_y))
                self.move_to(train, (cx, cy-1))
                self.t_enter((x, y))
            elif self.mechanic.map_array[x][y+1] == 1 and self.mechanic.map_array[x+1][y] == 1:  # w prawio
                self.t_exit((old_x, old_y))
                self.move_to(train, (cx, cy-1), 1)
                self.t_enter((x, y))
            elif self.mechanic.map_array[x][y+1] == 1 and self.mechanic.map_array[x-1][y] == 1:  # w lewo
                self.t_exit((old_x, old_y))
                self.move_to(train, (cx, cy-1), -1)
                self.t_enter((x, y))
            elif self.mechanic.map_array[x][y].id == 9:
                if self.mechanic.map_array[x][y].station_num == train.finish:
                    self.t_exit((old_x, old_y))
                    self.move_to(train, (cx, cy-1))
                    self.t_enter((x, y))
                    #self.map_score += train.get_value()
                    self.trains.remove(train)
                    self.t_exit((x, y))
                    self.add_value_to_score(train.get_value())
                    #print "Jeste w domku"

                else:
                    self.move_to(train, (cx, cy-1), 2)
            else:
                print "tu mnie nie powinno byc"
                train.if_moving = False
                train.can_move = False

        elif train.direction == 1:
            x, y = self.mechanic.get_center((cx+1, cy))
            if self.mechanic.map_array[x-1][y] == "_" and not self.mechanic.map_array[x][y].id == 9:
                train.if_moving = False
                train.can_move = False
                train.time = 20 #czas przed ponownym ruszeniem
                self.move_to(train, (cx, cy))
               # print "Nie moge jechac a jade"
            elif self.mechanic.map_array[x-1][y] == 1 and self.mechanic.map_array[x+1][y] == 1:  # prosto
                self.t_exit((old_x, old_y))
                self.move_to(train, (cx+1, cy))
                self.t_enter((x, y))
            elif self.mechanic.map_array[x-1][y] == 1 and self.mechanic.map_array[x][y+1] == 1:  # w prawio
                self.t_exit((old_x, old_y))
                self.move_to(train, (cx+1, cy), 1)
                self.t_enter((x, y))
            elif self.mechanic.map_array[x-1][y] == 1 and self.mechanic.map_array[x][y-1] == 1:  # w lewo
                self.t_exit((old_x, old_y))
                self.move_to(train, (cx+1, cy), -1)
                self.t_enter((x, y))
            elif self.mechanic.map_array[x][y].id == 9:
                if self.mechanic.map_array[x][y].station_num == train.finish:
                    self.t_exit((old_x, old_y))
                    self.move_to(train, (cx+1, cy))
                    self.t_enter((x, y))
                    #self.map_score += train.get_value()
                    self.trains.remove(train)
                    self.t_exit((x, y))
                    self.add_value_to_score(train.get_value())
                    #print "Jeste w domku"
                else:
                    self.move_to(train, (cx+1, cy), 2)
            else:
                print "tu mnie nie powinno byc"
                train.if_moving = False
                train.can_move = False

        elif train.direction == 2:
            x, y = self.mechanic.get_center((cx, cy+1))
            if self.mechanic.map_array[x][y-1] == "_" and not self.mechanic.map_array[x][y].id == 9:
                train.if_moving = False
                train.can_move = False
                train.time = 20 #czas przed ponownym ruszeniem
                self.move_to(train, (cx, cy))
                #print "Nie moge jechac a jade"
            elif self.mechanic.map_array[x][y-1] == 1 and self.mechanic.map_array[x][y+1] == 1:  # prosto
                self.t_exit((old_x, old_y))
                self.move_to(train, (cx, cy+1))
                self.t_enter((x, y))
            elif self.mechanic.map_array[x][y-1] == 1 and self.mechanic.map_array[x-1][y] == 1:  # w prawio
                self.t_exit((old_x, old_y))
                self.move_to(train, (cx, cy+1), 1)
                self.t_enter((x, y))
            elif self.mechanic.map_array[x][y-1] == 1 and self.mechanic.map_array[x+1][y] == 1:  # w lewo
                self.t_exit((old_x, old_y))
                self.move_to(train, (cx, cy+1), -1)
                self.t_enter((x, y))
            elif self.mechanic.map_array[x][y].id == 9:
                if self.mechanic.map_array[x][y].station_num == train.finish:
                    self.t_exit((old_x, old_y))
                    self.move_to(train, (cx, cy+1))
                    self.t_enter((x, y))
                    #self.map_score += train.get_value()
                    self.trains.remove(train)
                    self.t_exit((x, y))
                    self.add_value_to_score(train.get_value())
                    #print "Jeste w domku"
                else:
                    self.move_to(train, (cx, cy+1), 2)

            else:
                print "tu mnie nie powinno byc"
                train.if_moving = False
                train.can_move = False

        elif train.direction == 3:
            x, y = self.mechanic.get_center((cx-1, cy))
            if self.mechanic.map_array[x+1][y] == "_" and not self.mechanic.map_array[x][y].id == 9:
                train.if_moving = False
                train.can_move = False
                train.time = 20 #czas przed ponownym ruszeniem
                self.move_to(train, (cx, cy))
                #print "Nie moge jechac a jade"
            elif self.mechanic.map_array[x+1][y] == 1 and self.mechanic.map_array[x-1][y] == 1:  # prosto
                self.t_exit((old_x, old_y))
                self.move_to(train, (cx-1, cy))
                self.t_enter((x, y))
            elif self.mechanic.map_array[x+1][y] == 1 and self.mechanic.map_array[x][y-1] == 1:  # w prawio
                self.t_exit((old_x, old_y))
                self.move_to(train, (cx-1, cy), 1)
                self.t_enter((x, y))
            elif self.mechanic.map_array[x+1][y] == 1 and self.mechanic.map_array[x][y+1] == 1:  # w lewo
                self.t_exit((old_x, old_y))
                self.move_to(train, (cx-1, cy), -1)
                self.t_enter((x, y))
            elif self.mechanic.map_array[x][y].id == 9:
                if self.mechanic.map_array[x][y].station_num == train.finish:
                    self.t_exit((old_x, old_y))
                    self.move_to(train, (cx-1, cy))
                    self.t_enter((x, y))
                    #self.map_score += train.get_value()
                    self.trains.remove(train)
                    self.t_exit((x, y))
                    self.add_value_to_score(train.get_value())
                    #print "Jeste w domku"
                else:
                    self.move_to(train, (cx-1, cy), 2)

            else:
                print "tu mnie nie powinno byc"
                train.if_moving = False
                train.can_move = False
        else:
            print"ale nic nie robie"
        self.check_collision()