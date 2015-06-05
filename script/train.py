__author__ = 'Pawel'


from pygame import image as img
from pygame import transform as trans
import os

dir = os.path.dirname(__file__)


class Train(object):
    """
    Train Class
    """
    def __init__(self, start=None, finish=0, value=0):
        """
        :param start:
        :param finish:
        :param value:
        :return:
        """
        self.img = os.path.join(dir, r"images/train_1.png")
        self.speed = 4
        self.finish = finish
        self.if_moving = False
        self.can_move = False
        self.direction = start.rotation
        self.value = value
        self.x = start.x
        self.y = start.y
        self.animation = 120

    def change_direction(self, time):
        """
        Change direction by time
        :param time:
        :return:
        """
        self.direction = (self.direction + time) % 4

    def set_value(self, val):
        """
        Set value
        :param val:
        :return:
        """
        self.value = val

    def change_speed(self, val):
        """
        Change speed
        :param val:
        :return:
        """
        self.speed = val

    def get_pos(self):
        """
        Get position
        :return:
        """
        return self.x, self.y

    def animation_step(self):
        """
        Do animation step by self.speed
        :return:
        """
        if self.can_move:
            self.animation += self.speed
            if self.animation >= 64:
                self.if_moving = False
                self.animation = 0

    def set_pos(self, x, y):
        """
        Set position
        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y

    def get_image(self):
        """
        Get image with set rotation
        :return:
        """
        image = img.load(self.img).convert_alpha()
        image = trans.rotate(image, self.direction * (-90))
        return image

    def get_value(self):
        """
        Get value
        :return:
        """
        return self.value

    def get_speed(self):
        """
        Get speed
        :return:
        """
        return self.speed

    def get_animation(self):
        """
        Get animation step
        :return:
        """
        return self.animation

    def get_can_move(self):
        """
        Get can_move - boolean
        :return:
        """
        return self.can_move