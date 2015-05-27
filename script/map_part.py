__author__ = 'Pawel'

from images_control import ImagesControl
import random

'''

Zmienic image na zwykly int i przed rysowaniem zwracac sie do funkcij image control ktora zwroci Path
nie bedziesz trzymal obiektu w kazdym Part
Ograniczenie pamieci
'''


class Part(object):
    def __init__(self, b_t=0, rot=0, x=0, y=0):
        self.id = b_t
        self.rotation = rot
        self.max_rotation = 4
        self.state = random.randint(0, 1)
        self.x = x
        self.y = y
        self.max_state = 2
        self.design = 0
        self.train_on = False
        self.image = ImagesControl(b_t)
        if b_t == 0 or b_t == 1 or b_t == 2:
            self.state = 0
            self.max_state = 1
            if b_t == 0:
                self.design = random.randint(0, 4)

                #   self.rotation = random.randint(0, 4)

    def __str__(self):
        return str(self.id)

    def rotate(self, times=1):
        self.rotation = (self.rotation + times) % self.max_rotation

    def change_state(self):
        if not self.train_on:
            self.state = (self.state + 1) % self.max_state

    def get_image_path(self):
        return self.image.get_by_state(self.state)

    def get_rotation(self):
        return self.rotation

    def get_direction(self):
        pass
        #  if self.id ==
