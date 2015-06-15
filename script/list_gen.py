__author__ = 'Pawel'

from train_generator import TrainGen
from random import randint


class ListGen(TrainGen):
    def __init__(self, stages):
        TrainGen.__init__(self, stages)
        print self.max_stages
        self.train_list_file = open('train_lists/train_list_'+str(self.max_stages), "r")
        self.time = 10

    def generate(self, train_num):
        if self.timer() and train_num < 3:
            values = self.train_list_file.readline().split()
            start = values[0]
            finish = values[1]
            speed = values[2]
            return start, finish, speed
        return None, None, None

    def timer(self):
        if self.time < 0:
            self.time = randint(200, 300)
            return True
        else:
            self.time -= 1
            return False