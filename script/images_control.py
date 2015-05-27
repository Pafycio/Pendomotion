__author__ = 'Pawel'
'''
Tu lepiej by bylo zmienic na listy  !
w przypadku gdy obrazek bedzie mial wiecej niz 2 stany

'''
''' GLOBAL '''
path_0 = r"C:\Users\Pawel\PycharmProjects\Pendomotion\script\images\blank.png"
path_1 = r"C:\Users\Pawel\PycharmProjects\Pendomotion\script\images\straight.png"
path_2 = r"C:\Users\Pawel\PycharmProjects\Pendomotion\script\images\curve.png"
path_3 = r"C:\Users\Pawel\PycharmProjects\Pendomotion\script\images\straight_right_2.png"
path_3_1 = r"C:\Users\Pawel\PycharmProjects\Pendomotion\script\images\straight_right_1.png"
path_4 = r"C:\Users\Pawel\PycharmProjects\Pendomotion\script\images\straight_left_1.png"
path_4_1 = r"C:\Users\Pawel\PycharmProjects\Pendomotion\script\images\straight_left_2.png"
path_5 = r"C:\Users\Pawel\PycharmProjects\Pendomotion\script\images\cross_2.png"
path_5_1 = r"C:\Users\Pawel\PycharmProjects\Pendomotion\script\images\cross_1.png"
path_9_1 = r"C:\Users\Pawel\PycharmProjects\Pendomotion\script\images\station_1.png"
path_t = r"C:\Users\Pawel\PycharmProjects\Pendomotion\script\images\train_1.png"
no_pic = r"C:\Users\Pawel\PycharmProjects\Pendomotion\script\images\none.png"


class ImagesControl(object):
    def __init__(self, b_t):
        self.t = b_t
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
        if state == 0:
            return self.path_state_1
        elif state == 1:
            return self.path_state_2
        else:
            return no_pic

    def get_image_list(self):
        return [self.path_state_1, self.path_state_2]