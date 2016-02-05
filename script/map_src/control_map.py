from map_loader import MapLoader
from script.images_flyweight import ImagesFlyweight
from pygame import image as img
from pygame import transform as trans

__author__ = 'pfert'


class ControlMap(object):
    def __init__(self):
        self.map_id = 0
        self.map = None
        self.x = 0
        self.y = 0
        self.trains = []
        self.stations = []
        self.score = 0
        self.fail = 0
        self.success = 0
        self.img_ctrl = ImagesFlyweight()

    def on_update(self):
        for train in self.trains:
            x, y = train.get_pos()
            rot = self.get_direction(train.get_rot())
            if rot == 'North':
                if self.map[x][y-1].train_id != -1:
                    pass
            elif rot == 'East':
                if self.map[x+1][y].train_id != -1:
                    pass
            elif rot == 'South':
                if self.map[x][y+1].train_id != -1:
                    pass
            elif rot == 'West':
                if self.map[x-1][y].train_id != -1:
                    pass

    def on_render(self):
        pass

    def load_map(self, map_id):
        self.map_id = map_id
        loader = MapLoader(map_id)
        self.map = loader.get_map()
        self.stations = loader.get_stations()
        self.x, self.y = loader.get_map_size()

    def set_train_generator(self, generator):
        pass

    def get_image(self, x, y):
        curr_element = self.map[x][y]
        image_path = self.img_ctrl.get_image_by_id_state(str(curr_element.get_type()), curr_element.get_state())
        image = img.load(image_path).convert_alpha()
        image = trans.rotate(image, int(curr_element.get_rotation()) * (-90))
        return image

    def on_click(self, (x, y)):
        if x >= 640 or y >= 512:
            pass
        else:
            i = 0
            j = 0
            x -= 64
            while x > 0:
                i += 1
                x -= 64
            y -= 64
            while y > 0:
                j += 1
                y -= 64
            self.map[i][j].change_state()

    def get_direction(self, rot):
        if rot == 0:
            return "North"
        elif rot == 1:
            return 'East'
        elif rot == 2:
            return 'South'
        elif rot == 3:
            return 'West'