__author__ = 'Pawel'


from pygame import image as img
from pygame import transform as trans
import os

dir = os.path.dirname(__file__)


class Train(object):
    """
    Train Class
    """

    def __init__(self, speed, finish, if_moving, can_move,
                 unblock, direction, value, x, y, animation, time):
        """
        :param start:
        :param finish:
        :param value:
        :return:
        """
        self.img = os.path.join(dir, "images", "train_1.png")
        self.speed = speed
        self.finish = finish
        self.if_moving = if_moving
        self.can_move = can_move
        self.unblock = unblock
        self.direction = direction
        self.value = value
        self.x = x
        self.y = y
        self.animation = animation
        self.time = time

    def change_direction(self, time):
        """
        Change direction by time
        :param time:
        :return:
        """
        self.direction = (self.direction + time) % 4

    def time_to_start(self):
        """

        :return:
        """
        if self.time-1 == 0:
            self.unblock = True
            self.time -= 1
            return True
            #print "Odblokowany"

        elif self.time > 0:
            #print self.time
            self.unblock = False
            self.time -= 1
            return False

        else:
            return True

    def set_value(self, val):
        """
        Set value
        :param val:
        :return:
        """
        self.value = val

    def set_speed(self, val):
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

    def animation_step(self, speed):
        """
        Do animation step by self.speed
        :return:
        """
        if self.can_move:
            self.animation += speed
            if self.animation >= 64:
                self.if_moving = False
                self.animation = 1

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

    def set_strategy(self, can_move, if_moving):
        """
        :param can_move:
        :param if_moving:
        :return:
        """
        self.can_move = can_move
        self.if_moving = if_moving