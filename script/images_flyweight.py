__author__ = 'Pawel'

import os


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


class ImagesFlyweight(object):
    """Image Control Class"""
    def __init__(self):
        """
        :param block_type:
        :return:
        """
        self.type = None
        self.path_state_1 = no_pic
        self.path_state_2 = no_pic

    def get_image_by_id_state(self, block_type, state):
        self.type = block_type
        if self.type == 0:
            return path_0
        elif self.type == 1:
            return path_1
        elif self.type == 2:
            return path_2
        elif self.type == 3:
            if state == 0:
                return path_3
            elif state == 1:
                return path_3_1
        elif self.type == 4:
            if state == 0:
                return path_4
            elif state == 1:
                return path_4_1
        elif self.type == 5:
            if state == 0:
                return path_5
            elif state == 1:
                return path_5_1
        elif self.type == 9:
            return path_9_1
