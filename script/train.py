__author__ = 'Pawel'


from pygame import image as img
from pygame import transform as trans


class Train(object):
    def __init__(self, fin=0, val=0, station=None):
        self.img = r"C:\Users\Pawel\PycharmProjects\Pendomotion\script\images\train_1.png"
        self.speed = 1
        self.finish = fin
        self.if_moving = True
        self.if_crash = False
        self.direction = station.rotation
        self.value = val
        self.x = station.x
        self.y = station.y

    def change_direction(self, num):
        self.direction = (self.direction + num) % 4

    def set_value(self, val):
        self.value = val

    def change_speed(self, val):
        self.speed = val

    def get_pos(self):
        return self.x, self.y

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def get_image(self):
        image = img.load(self.img).convert_alpha()
        image = trans.rotate(image, self.direction * (-90))
        return image

    def get_value(self):
        return self.value