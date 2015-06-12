__author__ = 'Pawel'

import random


class Part(object):
    """
    Part Class
    """
    def __init__(self, block_type=0, rotation=0, x=0, y=0):
        """
        :param block_type:
        :param rotation:
        :param x:
        :param y:
        :return:
        """
        if block_type >= 10:
            raise IndexError('Index out of range')
        self.block_type = block_type
        self.rotation = rotation
        self.max_rotation = 4
        self.state = random.randint(0, 1)
        self.x = x
        self.y = y
        self.max_state = 2
        self.design = 0
        self.train_on = False
        self.station_num = None
        if block_type == 0 or block_type == 1 or block_type == 2:
            self.state = 0
            self.max_state = 1
            if block_type == 0:
                self.design = random.randint(0, 4)

                #   self.rotation = random.randint(0, 4)

    def __str__(self):
        """
        Return block type
        :return:
        """
        return str(self.block_type)

    def rotate(self, times=1):
        """
        Rotate by times
        :param times:
        :return:
        """
        self.rotation = (self.rotation + times) % self.max_rotation

    def change_state(self):
        """
        Change state
        :return:
        """
        if not self.train_on:
            self.state = (self.state + 1) % self.max_state


    def get_rotation(self):
        """
        Return rotation
        :return:
        """
        return self.rotation

    def train_enter(self):
        """
        Train on the Part (rails)
        :return:
        """
        if not self.train_on:
            self.train_on = True

    def train_exit(self):
        """
        Train off the Part (rails)
        :return:
        """
        self.train_on = False
