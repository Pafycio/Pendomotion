__author__ = 'Pawel'

from train_generator import TrainGen
from random import randint


class RandomGen(TrainGen):
    def __init__(self, stages):
        TrainGen.__init__(self, stages)
        print self.max_stages

    def generate(self, train_num):
        """
        Random generating trains with rand start and rand end
        :return:
        """
        start_stage = randint(0, self.max_stages)
        finish_stage = randint(0, self.max_stages)
        speed = randint(3, 8)
        gen_new = randint(0, 10000)
        if train_num == 0:
            return start_stage, finish_stage, speed
        elif train_num == 1 and gen_new <= 100:
            return start_stage, finish_stage, speed
        elif train_num == 2 and gen_new <= 10:
            return start_stage, finish_stage, speed
        else:
            return None, None, None