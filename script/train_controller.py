__author__ = 'Pawel'

from train_builder import TrainBuilder
from random_gen import RandomGen
from list_gen import ListGen
from random import randint


class TrainController(object):
    def __init__(self, mapa, generator):
        """
        :param mapa:
        :return:
        """
        self.trains = []
        self.stations = mapa.stations
        self.mechanic = mapa.mechanic
        self.train_build = TrainBuilder()
        self.map = mapa
        if generator:
            self.train_generator = RandomGen(len(self.map.stations))
        else:
            self.train_generator = ListGen(len(self.map.stations))

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
        """

        :return:
        """
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
        self.train_build.set_bool_values(False, True, False)
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
        start, finish, speed = self.train_generator.generate(len(self.trains))
        if start is not None:
            value = randint(100, 150)
            self.add_train(int(start), int(finish), int(value), int(speed))

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
                    self.map.add_crash()

    def train_finish(self, train):
        self.trains.remove(train)
        self.add_value_to_score(train.get_value())
        self.map.add_finish_train()

    def add_value_to_score(self, value):
        """

        :param value:
        :return:
        """
        self.map.map_score += value

    @staticmethod
    def move_to(train, (x, y), direction=0, can_move=True):
        """

        :param train:
        :param direction:
        :param can_move:
        :return:
        """
        train.if_moving = can_move
        train.can_move = can_move
        train.set_pos(x, y)
        train.change_direction(direction)

    def set_strategy(self, train):
        """

        :param train:
        :return:
        """

        if train.time_to_start():
            #  print "Cokolwiek"
            if not train.if_moving:
                #  print "1"
                self.check_move(train)

            if train.can_move and train.if_moving:
                train.animation_step(2)
                #  print "2"

            elif not train.can_move and not train.if_moving:
                train.animation_step(0)
                #  print "3"

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
        if train.unblock:
            #  print "Wystartowalen "+str(cx)+" "+str(cy)
            if train.can_move:
                if self.check_again(train) == 0:
                    print "jade w if"
                    self.move_to(train, (cx, cy))
                    train.unblock = False
            else:
                if self.check_again(train) == 0:
                    print "jade w else"
                    self.move_to(train, (cx, cy), False)
                    train.unblock = False

        elif train.direction == 0:
            self.check_upper(train)

        elif train.direction == 1:
            self.check_right(train)

        elif train.direction == 2:
            self.check_down(train)

        elif train.direction == 3:
            self.check_left(train)
        else:
            print"ale nic nie robie"
        self.check_collision()

    def check_upper(self, train):
        cx, cy = train.get_pos()
        x, y = self.mechanic.get_center((cx, cy-1))
        old_x, old_y = self.mechanic.get_center((cx, cy))

        if self.mechanic.map_array[x][y+1] == "_" and not self.mechanic.map_array[x][y].block_type == 9:
            train.if_moving = False
            train.can_move = False
            train.time = 20

        elif self.mechanic.map_array[x][y+1] == 1 and self.mechanic.map_array[x][y-1] == 1:  # prosto
            self.move_to_new_position(train, (old_x, old_y), (cx, cy-1), (x, y))

        elif self.mechanic.map_array[x][y+1] == 1 and self.mechanic.map_array[x+1][y] == 1:  # w prawio
            self.move_to_new_position(train, (old_x, old_y), (cx, cy-1), (x, y), 1)

        elif self.mechanic.map_array[x][y+1] == 1 and self.mechanic.map_array[x-1][y] == 1:  # w lewo
            self.move_to_new_position(train, (old_x, old_y), (cx, cy-1), (x, y), -1)

        elif self.mechanic.map_array[x][y].block_type == 9:
            if self.mechanic.map_array[x][y].station_num == train.finish:
                self.move_to_new_position(train, (old_x, old_y), (cx, cy-1), (x, y))
                self.t_exit((x, y))
                self.train_finish(train)

            else:
                self.move_to(train, (cx, cy-1), 2)
        else:
            print "tu mnie nie powinno byc"
            train.if_moving = False
            train.can_move = False

    def check_right(self, train):
        cx, cy = train.get_pos()
        x, y = self.mechanic.get_center((cx+1, cy))
        old_x, old_y = self.mechanic.get_center((cx, cy))

        if self.mechanic.map_array[x-1][y] == "_" and not self.mechanic.map_array[x][y].block_type == 9:
            train.if_moving = False
            train.can_move = False
            train.time = 20

        elif self.mechanic.map_array[x-1][y] == 1 and self.mechanic.map_array[x+1][y] == 1:  # prosto
            self.move_to_new_position(train, (old_x, old_y), (cx+1, cy), (x, y))

        elif self.mechanic.map_array[x-1][y] == 1 and self.mechanic.map_array[x][y+1] == 1:  # w prawio
            self.move_to_new_position(train, (old_x, old_y), (cx+1, cy), (x, y), 1)

        elif self.mechanic.map_array[x-1][y] == 1 and self.mechanic.map_array[x][y-1] == 1:  # w lewo
            self.move_to_new_position(train, (old_x, old_y), (cx+1, cy), (x, y), -1)

        elif self.mechanic.map_array[x][y].block_type == 9:
            if self.mechanic.map_array[x][y].station_num == train.finish:
                self.move_to_new_position(train, (old_x, old_y), (cx+1, cy), (x, y))
                self.t_exit((x, y))
                self.train_finish(train)
            else:
                self.move_to(train, (cx+1, cy), 2)
        else:
            print "tu mnie nie powinno byc"
            train.if_moving = False
            train.can_move = False

    def check_down(self, train):
        cx, cy = train.get_pos()
        x, y = self.mechanic.get_center((cx, cy+1))
        old_x, old_y = self.mechanic.get_center((cx, cy))

        if self.mechanic.map_array[x][y-1] == "_" and not self.mechanic.map_array[x][y].block_type == 9:
            train.if_moving = False
            train.can_move = False
            train.time = 20

        elif self.mechanic.map_array[x][y-1] == 1 and self.mechanic.map_array[x][y+1] == 1:  # prosto
            self.move_to_new_position(train, (old_x, old_y), (cx, cy+1), (x, y))

        elif self.mechanic.map_array[x][y-1] == 1 and self.mechanic.map_array[x-1][y] == 1:  # w prawio
            self.move_to_new_position(train, (old_x, old_y), (cx, cy+1), (x, y), 1)

        elif self.mechanic.map_array[x][y-1] == 1 and self.mechanic.map_array[x+1][y] == 1:  # w lewo
            self.move_to_new_position(train, (old_x, old_y), (cx, cy+1), (x, y), -1)

        elif self.mechanic.map_array[x][y].block_type == 9:
            if self.mechanic.map_array[x][y].station_num == train.finish:
                self.move_to_new_position(train, (old_x, old_y), (cx, cy+1), (x, y))
                self.t_exit((x, y))
                self.train_finish(train)
            else:
                self.move_to(train, (cx, cy+1), 2)

        else:
            print "tu mnie nie powinno byc"
            train.if_moving = False
            train.can_move = False

    def check_left(self, train):
        cx, cy = train.get_pos()
        old_x, old_y = self.mechanic.get_center((cx, cy))
        x, y = self.mechanic.get_center((cx-1, cy))
        if self.mechanic.map_array[x+1][y] == "_" and not self.mechanic.map_array[x][y].block_type == 9:
            train.if_moving = False
            train.can_move = False
            train.time = 20

        elif self.mechanic.map_array[x+1][y] == 1 and self.mechanic.map_array[x-1][y] == 1:  # prosto
            self.move_to_new_position(train, (old_x, old_y), (cx-1, cy), (x, y))

        elif self.mechanic.map_array[x+1][y] == 1 and self.mechanic.map_array[x][y-1] == 1:  # w prawio
            self.move_to_new_position(train, (old_x, old_y), (cx-1, cy), (x, y), 1)

        elif self.mechanic.map_array[x+1][y] == 1 and self.mechanic.map_array[x][y+1] == 1:  # w lewo
            self.move_to_new_position(train, (old_x, old_y), (cx-1, cy), (x, y), -1)

        elif self.mechanic.map_array[x][y].block_type == 9:
            if self.mechanic.map_array[x][y].station_num == train.finish:
                self.move_to_new_position(train, (old_x, old_y), (cx-1, cy), (x, y))
                self.t_exit((x, y))
                self.train_finish(train)
            else:
                self.move_to(train, (cx-1, cy), 2)

        else:
            print "tu mnie nie powinno byc"
            train.if_moving = False
            train.can_move = False

    def move_to_new_position(self, train, (old_x, old_y), (cx, cy), (x, y), direction=0):
        self.t_exit((old_x, old_y))
        self.move_to(train, (cx, cy), direction)
        self.t_enter((x, y))

    def check_again(self, train):
        couter = 0
        cx, cy = train.get_pos()
        x, y = self.mechanic.get_center((cx, cy-1))
        if self.mechanic.map_array[x][y+1] == "_" and not self.mechanic.map_array[x][y].block_type == 9 and train.direction == 0:
            couter += 1

        cx, cy = train.get_pos()
        x, y = self.mechanic.get_center((cx+1, cy))
        if self.mechanic.map_array[x-1][y] == "_" and not self.mechanic.map_array[x][y].block_type == 9 and train.direction == 1:
            couter += 1

        cx, cy = train.get_pos()
        x, y = self.mechanic.get_center((cx, cy+1))
        print cx, cy
        print x, y
        if self.mechanic.map_array[x][y-1] == "_" and not self.mechanic.map_array[x][y].block_type == 9 and train.direction == 2:
            couter += 1

        cx, cy = train.get_pos()
        x, y = self.mechanic.get_center((cx-1, cy))
        if self.mechanic.map_array[x+1][y] == "_" and not self.mechanic.map_array[x][y].block_type == 9 and train.direction == 3:
            couter += 1

        return couter