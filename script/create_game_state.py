__author__ = 'Pawel'

import pygame
from state import State

light_grey = (200, 200, 209)
black = (0, 0, 0)

green = (0, 150, 50)
bright_green = (0, 200, 0)

red = (200, 0, 20)
bright_red = (230, 0, 0)


class CreateGame(State):
    """
    CREATE GAME STATE
    """
    def __init__(self, surf, prev):
        """
        :param surf:
        :param prev:
        :return:
        """
        State.__init__(self, surf, prev)
        self.random = True
        self.train = 6
        self.crash = 4
        self.map = "2"

    def on_update(self):
        """

        :return:
        """
        pass

    def on_render(self):
        """

        :return:
        """
        self.surf.fill(light_grey)
        title_font = pygame.font.Font(None, 50)
        copy_font = pygame.font.Font(None, 20)
        button_font = pygame.font.Font(None, 30)
        title = title_font.render("PENDOMOTION", 10, black)
        self.surf.blit(title, (190, 100))
        mouse = pygame.mouse.get_pos()

        ''' CHOICE GENERATING TYPE  '''
        train_gen = button_font.render("Choice type of train generating system.", 10, black)
        self.surf.blit(train_gen, (50, 185))

        if self.random:
            pygame.draw.rect(self.surf, bright_green, (460, 170, 80, 50))
            pygame.draw.rect(self.surf, green, (540, 170, 80, 50))
        else:
            pygame.draw.rect(self.surf, green, (460, 170, 80, 50))
            pygame.draw.rect(self.surf, bright_green, (540, 170, 80, 50))

        start_test = button_font.render("RAND", 10, black)
        self.surf.blit(start_test, (470, 185))

        start_test = button_font.render("LIST", 10, black)
        self.surf.blit(start_test, (555, 185))

        ''' NUMBER OF TRAINS TO WIN '''
        train_num = button_font.render("Number of trains to win.", 10, black)
        self.surf.blit(train_num, (50, 243))

        number = title_font.render(str(self.train), 10, black)
        self.surf.blit(number, (530, 235))

        if 580+30 > mouse[0] > 580 and 245+30 > mouse[1] > 245:
            pygame.draw.rect(self.surf, bright_green, (580, 245, 30, 10))
            pygame.draw.rect(self.surf, bright_green, (590, 235, 10, 30))
        else:
            pygame.draw.rect(self.surf, green, (580, 245, 30, 10))
            pygame.draw.rect(self.surf, green, (590, 235, 10, 30))

        if 470+30 > mouse[0] > 470 and 245+10 > mouse[1] > 245:
            pygame.draw.rect(self.surf, bright_red, (470, 245, 30, 10))
        else:
            pygame.draw.rect(self.surf, red, (470, 245, 30, 10))

        ''' NUMBER OF CRASH TO LOSE '''
        crash_num = button_font.render("Number of crashes to lose.", 10, black)
        self.surf.blit(crash_num, (50, 301))

        number = title_font.render(str(self.crash), 10, black)
        self.surf.blit(number, (530, 294))

        if 580+30 > mouse[0] > 580 and 303+30 > mouse[1] > 303:
            pygame.draw.rect(self.surf, bright_green, (580, 303, 30, 10))
            pygame.draw.rect(self.surf, bright_green, (590, 293, 10, 30))
        else:
            pygame.draw.rect(self.surf, green, (580, 303, 30, 10))
            pygame.draw.rect(self.surf, green, (590, 293, 10, 30))

        if 470+30 > mouse[0] > 470 and 303+10 > mouse[1] > 303:
            pygame.draw.rect(self.surf, bright_red, (470, 303, 30, 10))
        else:
            pygame.draw.rect(self.surf, red, (470, 303, 30, 10))
        ''' BUTTONS '''
        if 200+240 > mouse[0] > 200 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(self.surf, bright_green, (200, 400, 240, 50))
        else:
            pygame.draw.rect(self.surf, green, (200, 400, 240, 50))

        start_test = button_font.render("START", 10, black)
        self.surf.blit(start_test, (288, 415))

        if 200+240 > mouse[0] > 200 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(self.surf, bright_red, (200, 500, 240, 50))
        else:
            pygame.draw.rect(self.surf, red, (200, 500, 240, 50))

        start_test = button_font.render("BACK", 10, black)
        self.surf.blit(start_test, (296, 515))

        title = copy_font.render("copyright Pawel Fert", 10, black)
        self.surf.blit(title, (240, 615))
        pygame.display.flip()

    def on_event(self, event):
        """
        :param event:
        :return:
        """
        if event.type == pygame.QUIT:
            return "EXIT"
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 460+80 > mouse[0] > 460 and 170+50 > mouse[1] > 170:
                self.random = True
            elif 540+80 > mouse[0] > 540 and 170+50 > mouse[1] > 170:
                self.random = False
            elif 580+30 > mouse[0] > 580 and 245+30 > mouse[1] > 245:
                self.add_train(1)
            elif 470+30 > mouse[0] > 470 and 245+10 > mouse[1] > 245:
                self.add_train(-1)
            elif 580+30 > mouse[0] > 580 and 303+30 > mouse[1] > 303:
                self.add_crash(1)
            elif 470+30 > mouse[0] > 470 and 303+10 > mouse[1] > 303:
                self.add_crash(-1)
            elif 200+240 > mouse[0] > 200 and 400+50 > mouse[1] > 400:
                return "GAME"
            elif 200+240 > mouse[0] > 200 and 500+50 > mouse[1] > 500:
                return "PREV"
        return "NONE"

    def add_train(self, value):
        """

        :param value:
        :return:
        """
        self.train += value
        if self.train < 1:
            self.train = 1

    def add_crash(self, value):
        """

        :param value:
        :return:
        """
        self.crash += value
        if self.crash < 1:
            self.crash = 1