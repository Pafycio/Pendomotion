__author__ = 'Pawel'

import pygame
from map import Map
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
width = 64
height = 64
margin = 0


class App():
    def __init__(self):
        """
        init game
        :return:
        """
        self._running = True
        self._display_surf = None
        self.fps_limit = 60
        self.clock = None
        self.map = Map("2")  # numer mapy
        self.size = self.weight, self.height = 640, 700

    def on_init(self):
        """
        :return:
        """
        pygame.init()
        self.clock = pygame.time.Clock()
        self._display_surf = pygame.display.set_mode(self.size)
        self._running = True
        self.map.load_map()

    def on_event(self, event):
        """
        :param event:
        :return:
        """
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.map.part_on_click(pygame.mouse.get_pos())

    def on_loop(self):
        """
        :return:
        """
        self.map.train_control.on_loop()

    def on_render(self):
        """
        :return:
        """
        self.score_font = pygame.font.Font(None, 36)
        self.map_font = pygame.font.Font(None, 20)
        self._display_surf.fill(black)
        for col in range(self.map.y):
            for row in range(0, self.map.x):
                image = self.map.get_image((col, row))
                self._display_surf.blit(image, (col*64, row*64))
                if self.map.get_id((col, row)) == 9:
                    text = self.score_font.render(str(self.map.get_station_num((col, row))), 1, white)
                    self._display_surf.blit(text, (col*64, row*64))

        for i in self.map.train_control.trains:
            if i.if_moving and i.can_move:
                if i.direction == 0:
                    self.draw_train(i, 0, -1)
                elif i.direction == 1:
                    self.draw_train(i, 1, 0)
                elif i.direction == 2:
                    self.draw_train(i, 0, 1)
                elif i.direction == 3:
                    self.draw_train(i, -1, 0)
            else:
                self.draw_train(i, 0, 0)

        score_text = self.score_font.render("SCORE : "+str(self.map.map_score), 1, white)

        self._display_surf.blit(score_text, (20, 530))

        self.clock.tick(60)

        pygame.display.flip()

    def on_clean_up(self):
        """

        :return:
        """
        pygame.quit()

    def draw_train(self, train, move_x, move_y):
        """
        :param train:
        :param move_x:
        :param move_y:
        :return:
        """
        #print str(train.get_animation())
        if train.if_moving:
            self._display_surf.blit(train.get_image(),
                                    (train.x*64+(move_x*train.get_animation()),
                                    train.y*64+(move_y*train.get_animation())))
            text = self.score_font.render(str(train.finish), 1, white)
            self._display_surf.blit(text,
                                    (train.x*64+(move_x*train.get_animation()),
                                     train.y*64+(move_y*train.get_animation())))
        elif not train.if_moving:
            self._display_surf.blit(train.get_image(),
                                    (train.x*64,
                                    train.y*64))
            text = self.score_font.render(str(train.finish), 1, white)
            self._display_surf.blit(text,
                                    (train.x*64,
                                     train.y*64))

    def on_execute(self):
        """

        :return:
        """
        if self.on_init():
            self._running = False

        while self._running:
            self.clock.tick(self.fps_limit)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()


        self.on_clean_up()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()