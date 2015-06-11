__author__ = 'Pawel'

from train import Train


class TrainBuilder(object):
    def __init__(self):
        """
        :param start:
        :param finish:
        :param value:
        :return:
        """
        self.img = None
        self.speed = None
        self.start = None
        self.finish = None
        self.if_moving = None
        self.can_move = None
        self.unblock = None
        self.direction = None
        self.value = None
        self.x = None
        self.y = None
        self.animation = None
        self.time = None

    def set_start_station(self, station):
        """

        :param station:
        :return:
        """
        self.start = station
        self.direction = station.rotation
        self.x = station.x
        self.y = station.y

    def set_finish_station(self, station):
        """

        :param station:
        :return:
        """
        self.finish = station

    def set_speed(self, speed):
        """

        :param speed:
        :return:
        """
        self.speed = speed

    def set_value(self, value):
        """

        :param value:
        :return:
        """
        self.value = value

    def set_bool_values(self, if_moving, can_move, unblock):
        """

        :param if_moving:
        :param can_move:
        :param unblock:
        :return:
        """
        self.if_moving = if_moving
        self.can_move = can_move
        self.unblock = unblock

    def set_img_id(self, img_id):
        """

        :param img_id:
        :return:
        """
        self.img = img_id

    def set_animation(self, animation):
        """

        :param animation:
        :return:
        """
        self.animation = animation

    def set_time(self, time):
        """

        :param time:
        :return:
        """
        self.time = time

    def create_train(self):
        """

        :return:
        """
        return Train(self.speed, self.start, self.finish, self.if_moving, self.can_move,
                     self.unblock, self.direction, self.value, self.x, self.y,
                     self.animation, self.time)