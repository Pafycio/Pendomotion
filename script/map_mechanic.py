__author__ = 'Pawel'


class MapMechanic(object):
    """

    """
    def __init__(self, (x, y)):
        self.x = x*3
        self.y = y*3
        self.map_array = [["_" for i in xrange(self.x)] for j in xrange(self.y)]

    def add_at(self, (x, y), obj):
        (x, y) = self.get_center((x, y))
        self.map_array[x][y] = obj
        self.set_mechanic_part((x, y), obj.block_type, obj.rotation, obj.state)

    def get_center(self, (x, y)):
        if x*3+1 == 1 and y*3+1 == 1:
            return (1, 1)
        elif 3*x+1 == 1 and 3*x+1 > self.y:
            return (1, self.y-2)
        elif 3*x+1 == self.x and y*3+1 == 1:
            return (self.x-2, 1)
        elif 3*x+1 == self.x and y*3+1 == self.y:
            return (self.x-2, self.y-2)
        else:
            return (x*3+1, y*3+1)

    def change_state(self, (x, y)):
        (x, y) = self.get_center((x, y))
        obj = self.map_array[x][y]
        obj.change_state()

        self.set_mechanic_part((x, y), obj.block_type, obj.rotation, obj.state)

    def set_mechanic_part(self, (x, y), t_b, rot, state):
        c = (x, y)
        if t_b == 1:
            if rot == 0 or rot == 2:
                self.draw_straight_vertically(c)
            elif rot == 1 or rot == 3:
                self.draw_straight_horizontally(c)

        elif t_b == 2:
            if rot == 3:
                self.draw_curve_bot_right(c)
            elif rot == 2:
                self.draw_curve_bot_left(c)
            elif rot == 1:
                self.draw_curve_top_left(c)
            elif rot == 0:
                self.draw_curve_top_right(c)

        elif t_b == 3:
            if rot == 0:
                if state == 0:
                    self.draw_straight_vertically(c)
                elif state == 1:
                    self.draw_curve_top_right(c)
            elif rot == 1:
                if state == 0:
                    self.draw_straight_horizontally(c)
                elif state == 1:
                    self.draw_curve_top_left(c)
            elif rot == 2:
                if state == 0:
                    self.draw_straight_vertically(c)
                elif state == 1:
                    self.draw_curve_bot_left(c)
            elif rot == 3:
                if state == 0:
                    self.draw_straight_horizontally(c)
                elif state == 1:
                    self.draw_curve_bot_right(c)

        elif t_b == 4:
            if rot == 0:
                if state == 0:
                    self.draw_straight_vertically(c)
                elif state == 1:
                    self.draw_curve_top_left(c)
            elif rot == 1:
                if state == 0:
                    self.draw_straight_horizontally(c)
                elif state == 1:
                    self.draw_curve_bot_left(c)
            elif rot == 2:
                if state == 0:
                    self.draw_straight_vertically(c)
                elif state == 1:
                    self.draw_curve_bot_right(c)
            elif rot == 3:
                if state == 0:
                    self.draw_straight_horizontally(c)
                elif state == 1:
                    self.draw_curve_top_right(c)
        elif t_b == 5:
            if rot == 0 or rot == 2:
                if state == 0:
                    self.draw_straight_horizontally(c)
                elif state == 1:
                    self.draw_straight_vertically(c)
            elif rot == 1 or rot == 3:
                if state == 0:
                    self.draw_straight_horizontally(c)
                elif state == 1:
                    self.draw_straight_vertically(c)

    def draw_straight_vertically(self, (x, y)):
        self.map_array[x][y-1] = 1
        self.map_array[x][y+1] = 1
        self.map_array[x-1][y] = "_"
        self.map_array[x+1][y] = "_"

    def draw_straight_horizontally(self, (x, y)):
        self.map_array[x-1][y] = 1
        self.map_array[x+1][y] = 1
        self.map_array[x][y+1] = "_"
        self.map_array[x][y-1] = "_"

    def draw_curve_bot_right(self, (x, y)):
        self.map_array[x][y-1] = 1
        self.map_array[x+1][y] = 1
        self.map_array[x][y+1] = "_"
        self.map_array[x-1][y] = "_"

    def draw_curve_bot_left(self, (x, y)):
        self.map_array[x][y-1] = 1
        self.map_array[x-1][y] = 1
        self.map_array[x][y+1] = "_"
        self.map_array[x+1][y] = "_"

    def draw_curve_top_left(self, (x, y)):
        self.map_array[x][y+1] = 1
        self.map_array[x-1][y] = 1
        self.map_array[x][y-1] = "_"
        self.map_array[x+1][y] = "_"

    def draw_curve_top_right(self, (x, y)):
        self.map_array[x][y+1] = 1
        self.map_array[x+1][y] = 1
        self.map_array[x][y-1] = "_"
        self.map_array[x-1][y] = "_"