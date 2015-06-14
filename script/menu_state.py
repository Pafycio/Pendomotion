__author__ = 'Pawel'

import pygame
from state import State

light_grey = (200, 200, 209)
black = (0, 0, 0)

green = (0, 150, 50)
bright_green = (0, 200, 0)

red = (200, 0, 20)
bright_red = (230, 0, 0)


class Menu(State):
    """
    MENU STATE
    """
    def __init__(self, surf, prev):
        """

        :param surf:
        :param prev:
        """
        State.__init__(self, surf, prev)

    def on_update(self):
        """


        """
        pass

    def on_render(self):
        """

        """
        self.surf.fill(light_grey)
        title_font = pygame.font.Font(None, 50)
        copy_font = pygame.font.Font(None, 20)
        button_font = pygame.font.Font(None, 30)
        title = title_font.render("PENDOMOTION", 10, black)
        self.surf.blit(title, (190, 100))
        mouse = pygame.mouse.get_pos()
        if 200+240 > mouse[0] > 200 and 200+50 > mouse[1] > 200:
            pygame.draw.rect(self.surf, bright_green, (200, 200, 240, 50))
        else:
            pygame.draw.rect(self.surf, green, (200, 200, 240, 50))

        start_test = button_font.render("CREATE GAME", 10, black)
        self.surf.blit(start_test, (242, 215))

        if 200+240 > mouse[0] > 200 and 300+50 > mouse[1] > 300:
            pygame.draw.rect(self.surf, bright_red, (200, 300, 240, 50))
        else:
            pygame.draw.rect(self.surf, red, (200, 300, 240, 50))

        start_test = button_font.render("EXIT", 10, black)
        self.surf.blit(start_test, (303, 315))

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
            if 200+240 > mouse[0] > 200 and 200+50 > mouse[1] > 200:
                return "CREATE"
            elif 200+240 > mouse[0] > 200 and 300+50 > mouse[1] > 300:
                return "EXIT"
        return "NONE"