__author__ = 'Pawel'

import pygame
from map import Map
from state import State
from pygame import image as img
from script.map_src.control_map import ControlMap
from random_gen import RandomGen
from list_gen import ListGen
black = (0, 0, 0)
white = (255, 255, 255)


class Game(State):
    """
    GAME STATE
    """
    def __init__(self, surf, prev):
        State.__init__(self, surf, prev)
        self.generator = self.prev_state.random
        self.max_trains = self.prev_state.train
        self.max_crash = self.prev_state.crash
        self.pause = False
        self.end = False
        self.map_controller = ControlMap()
        self.map_controller.load_map(self.prev_state.cur_map)
        self.map_controller.set_train_generator(self.generator)

    def on_update(self):
        """

        :return:
        """
        self.map_controller.on_update()

    def on_render(self):
        """

        :return:
        """
        score_font = pygame.font.Font(None, 36)
        number_font = pygame.font.Font(None, 25)
        if self.map_controller.success >= self.max_trains:
            s = pygame.Surface((640, 512))
            s.set_alpha(35)
            s.fill((200, 200, 200))
            self.surf.blit(s, (0, 0))
            text_c = score_font.render("LEVEL COMPLITED !", 10, black)
            self.surf.blit(text_c, (200, 300))
            text_c = score_font.render("SCORE : "+str(self.map_controller.score), 10, black)
            self.surf.blit(text_c, (200, 350))
            self.end = True
        elif self.map_controller.fail >= self.max_crash:
            s = pygame.Surface((640, 512))
            s.set_alpha(35)
            s.fill((200, 200, 200))
            self.surf.blit(s, (0, 0))
            text_l = score_font.render("YOU LOSE !", 10, black)
            self.surf.blit(text_l, (250, 300))
            self.end = True
        elif not self.pause:
            self.surf.fill(black)
            for col in range(self.map_controller.y):
                for row in range(0, self.map_controller.x):
                    image = self.map_controller.get_image(col, row)
                    self.surf.blit(image, (col*64, row*64))
                    if "Station" in self.map_controller.map[col][row].get_type():

                        station_num = self.map_controller.map[col][row].get_type().split('_')[1]
                        text = number_font.render(str(station_num), 1, white)
                        if self.map_controller.stations[int(station_num)].rotation == 0:
                            self.surf.blit(text, (col*64+8, row*64+38))
                        elif self.map_controller.stations[int(station_num)].rotation == 1:
                            self.surf.blit(text, (col*64+14, row*64+4))
                        elif self.map_controller.stations[int(station_num)].rotation == 2:
                            self.surf.blit(text, (col*64+47, row*64+10))
                        elif self.map_controller.stations[int(station_num)].rotation == 3:
                            self.surf.blit(text, (col*64+41, row*64+44))

            for i in self.map_controller.trains:
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
        elif self.pause:
            s = pygame.Surface((640, 512))
            s.set_alpha(35)
            s.fill((200, 200, 200))
            self.surf.blit(s, (0, 0))
            text = score_font.render("GAME PAUSED", 10, black)
            self.surf.blit(text, (230, 300))

        score_text = score_font.render("SCORE : "+str(self.map_controller.score), 1, white)
        train_text = score_font.render("TRAIN : "+str(self.map_controller.success)+""
                                       " / "+str(self.max_trains), 1, white)
        crash_text = score_font.render("CRASH : "+str(self.map_controller.fail)+""
                                       " / "+str(self.max_crash), 1, white)

        self.surf.blit(score_text, (20, 530))
        self.surf.blit(train_text, (20, 560))
        self.surf.blit(crash_text, (20, 590))

        pygame.display.flip()

    def on_event(self, event):
        """

        :param event:
        :return:
        """
        if event.type == pygame.QUIT:
            return "EXIT"
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.map_controller.on_click(pygame.mouse.get_pos())
            if self.end:
                return "MENU"
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            if self.pause:
                self.pause = False
            elif not self.pause:
                self.pause = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return "PAUSE"

        return "NONE"

    def draw_train(self, train, move_x, move_y):
        """
        :param train:
        :param move_x:
        :param move_y:
        :return:
        """
        score_font = pygame.font.Font(None, 36)
        if train.if_moving:
            self.surf.blit(train.get_image(),
                           (train.x*64+(move_x*train.get_animation()),
                            train.y*64+(move_y*train.get_animation())))
            text = score_font.render(str(train.finish), 1, white)
            self.surf.blit(text,
                           (train.x*64+(move_x*train.get_animation()),
                            train.y*64+(move_y*train.get_animation())))
            train.animation_step(3)
        elif not train.if_moving:

            self.surf.blit(train.get_image(),
                           (train.x*64,
                            train.y*64))
            text = score_font.render(str(train.finish), 1, white)
            self.surf.blit(text,
                           (train.x*64,
                            train.y*64))
            train.animation_step(0)