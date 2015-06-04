__author__ = 'Pawel'


from pygame import image as img
from pygame import transform as trans


class Train(object):
    def __init__(self, start=None, finish=0, value=0):
        self.img = r"C:\Users\Pawel\PycharmProjects\Pendomotion\script\images\train_1.png"
        self.speed = 4
        self.finish = finish
        self.if_moving = False
        self.can_move = False
        self.direction = start.rotation
        self.value = value
        self.x = start.x
        self.y = start.y
        self.animation = 0

    def change_direction(self, num):
        self.direction = (self.direction + num) % 4

    def set_value(self, val):
        self.value = val

    def change_speed(self, val):
        self.speed = val

    def get_pos(self):
        return self.x, self.y

    def animation_step(self):
        if self.can_move:
            self.animation += self.speed
            if self.animation >= 64:
                self.if_moving = False
                self.animation = 0

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def get_image(self):
        image = img.load(self.img).convert_alpha()
        image = trans.rotate(image, self.direction * (-90))
        return image

    def get_value(self):
        return self.value

    def get_speed(self):
        return self.speed

    def get_animation(self):
        return self.animation

    def get_can_move(self):
        return self.can_move