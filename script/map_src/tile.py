__author__ = 'pfert'

NO_TRAIN = -1


class Tile(object):
    def __init__(self, block_type='', rotation=0, max_state=1, state=0, style=0):
        self.style = style
        self.type = block_type
        self.rotation = rotation
        self.state = state
        self.max_state = max_state

        self.train_id = NO_TRAIN

    def __str__(self):
        return str(self.type)

    def get_type(self):
        return self.type

    def get_state(self):
        return self.state

    def rotate(self, times=1):
        """
        Rotate by times
        :param times:
        :return:
        """
        self.rotation = (self.rotation + times) % 4

    def get_rotation(self):
        """
        Return rotation
        :return:
        """
        return self.rotation

    def change_state(self):
        if self.train_id == NO_TRAIN:
            self.state = (self.state + 1) % self.max_state

    def train_enter(self, train_id):
        """
        Train on the Part (rails)
        :return:
        """
        if self.train_id == NO_TRAIN:
            self.train_id = train_id

    def train_exit(self):
        """
        Train off the Part (rails)
        :return:
        """
        self.train_id = NO_TRAIN
