__author__ = 'Pawel'

import os

'''
Tu lepiej by bylo zmienic na listy  !
w przypadku gdy obrazek bedzie mial wiecej niz 2 stany

'''
''' GLOBAL '''
dir = os.path.dirname(__file__)

path_0 = os.path.join(dir, "images", "blank.png")
path_1 = os.path.join(dir, "images", "straight.png")
path_2 = os.path.join(dir, "images", "curve.png")
path_3 = os.path.join(dir, "images", "straight_right_2.png")
path_3_1 = os.path.join(dir, "images", "straight_right_1.png")
path_4 = os.path.join(dir, "images", "straight_left_1.png")
path_4_1 = os.path.join(dir, "images", "straight_left_2.png")
path_5 = os.path.join(dir, "images", "cross_2.png")
path_5_1 = os.path.join(dir, "images", "cross_1.png")
path_9_1 = os.path.join(dir, "images", "station_1.png")
path_t = os.path.join(dir, "images", "train_1.png")
no_pic = os.path.join(dir, "images", "none.png")


class ImagesControl(object):
    """Image Control Class"""
    def __init__(self, block_type):
        """
        :param block_type:
        :return:
        """
        self.t = block_type
        self.path_state_1 = no_pic
        self.path_state_2 = no_pic
        if self.t == 0:
            self.path_state_1 = path_0
        elif self.t == 1:
            self.path_state_1 = path_1
        elif self.t == 2:
            self.path_state_1 = path_2
        elif self.t == 3:
            self.path_state_1 = path_3
            self.path_state_2 = path_3_1
        elif self.t == 4:
            self.path_state_1 = path_4
            self.path_state_2 = path_4_1
        elif self.t == 5:
            self.path_state_1 = path_5
            self.path_state_2 = path_5_1
        elif self.t == 9:
            self.path_state_1 = path_9_1
            self.path_state_2 = path_9_1

    def get_by_state(self, state):
        """
        Return path to image on state
        :param state:
        :return:
        """
        if state == 0:
            return self.path_state_1
        elif state == 1:
            return self.path_state_2
        else:
            return no_pic

    def get_image_list(self):
        """
        List of paths to images
        :return:
        """
        return [self.path_state_1, self.path_state_2]
