__author__ = 'Pawel'

import pygame
from map import Map
from state import State

black = (0, 0, 0)
white = (255, 255, 255)


class Game(State):
    def __init__(self, surf, prev):
        State.__init__(self, surf, prev)
        self.random = self.prev_state.random
        self.max_trains = self.prev_state.train
        self.max_crash = self.prev_state.crash
        self.map = Map(self.prev_state.map)
        self.map.load_map()
        self.pause = False
        self.end = False

    def on_update(self):
        pass

    def on_render(self):
        self.score_font = pygame.font.Font(None, 36)
        self.map_font = pygame.font.Font(None, 20)
        if self.map.train_in_state >= self.max_trains:
            s = pygame.Surface((640, 512))  # the size of your rect
            s.set_alpha(35)                # alpha level
            s.fill((200, 200, 200))           # this fills the entire surface
            self.surf.blit(s, (0, 0))    # (0,0) are the top-left coordinates
            text_c = self.score_font.render("LEVEL COMPLITED !", 10, black)
            self.surf.blit(text_c, (200, 300))
            self.end = True
        elif self.map.crash >= self.max_crash:
            s = pygame.Surface((640, 512))  # the size of your rect
            s.set_alpha(35)                # alpha level
            s.fill((200, 200, 200))           # this fills the entire surface
            self.surf.blit(s, (0, 0))    # (0,0) are the top-left coordinates
            text_l = self.score_font.render("YOU LOSE !", 10, black)
            self.surf.blit(text_l, (250, 300))
            self.end = True
        elif not self.pause:
            self.map.train_control.on_loop()
            self.surf.fill(black)
            for col in range(self.map.y):
                for row in range(0, self.map.x):
                    image = self.map.get_image((col, row))
                    self.surf.blit(image, (col*64, row*64))
                    if self.map.get_id((col, row)) == 9:
                        text = self.score_font.render(str(self.map.get_station_num((col, row))), 1, white)
                        self.surf.blit(text, (col*64, row*64))

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
                    #print "tu rysuje przeskok"
                    self.draw_train(i, 0, 0)
        elif self.pause:
            s = pygame.Surface((640, 512))  # the size of your rect
            s.set_alpha(35)                # alpha level
            s.fill((200, 200, 200))           # this fills the entire surface
            self.surf.blit(s, (0, 0))    # (0,0) are the top-left coordinates
            text = self.score_font.render("GAME PAUSED", 10, black)
            self.surf.blit(text, (230, 300))

        score_text = self.score_font.render("SCORE : "+str(self.map.map_score), 1, white)
        train_text = self.score_font.render("TRAIN : "+str(self.map.train_in_state)+""
                                            " / "+str(self.max_trains), 1, white)
        crash_text = self.score_font.render("CRASH : "+str(self.map.crash)+""
                                            " / "+str(self.max_crash), 1, white)

        self.surf.blit(score_text, (20, 530))
        self.surf.blit(train_text, (20, 560))
        self.surf.blit(crash_text, (20, 590))

        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            return "EXIT"
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.map.part_on_click(pygame.mouse.get_pos())
            if self.end:
                return "MENU"
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            print "Pressed P"
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
        if train.if_moving:
            self.surf.blit(train.get_image(),
                           (train.x*64+(move_x*train.get_animation()),
                            train.y*64+(move_y*train.get_animation())))
            text = self.score_font.render(str(train.finish), 1, white)
            self.surf.blit(text,
                           (train.x*64+(move_x*train.get_animation()),
                            train.y*64+(move_y*train.get_animation())))
            train.animation_step(3)
        elif not train.if_moving:
            #print "tak to ten stojacy jebie wszystko "+str(train.x)+" "+str(train.y)
            self.surf.blit(train.get_image(),
                           (train.x*64,
                            train.y*64))
            text = self.score_font.render(str(train.finish), 1, white)
            self.surf.blit(text,
                           (train.x*64,
                            train.y*64))
            train.animation_step(0)