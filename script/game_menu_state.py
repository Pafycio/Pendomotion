__author__ = 'Pawel'

import pygame
from state import State

black = (0, 0, 0)
green = (0, 150, 50)
bright_green = (0, 200, 0)

red = (200, 0, 20)
bright_red = (230, 0, 0)


class GameMenu(State):
    def __init__(self, surf, prev):
        State.__init__(self, surf, prev)

    def on_update(self):
        pass

    def on_render(self):
        button_font = pygame.font.Font(None, 30)
        s = pygame.Surface((640, 512))
        s.set_alpha(35)
        s.fill((200, 200, 200))
        self.surf.blit(s, (0, 0))
        text_c = button_font.render("GAME MENU", 10, black)
        self.surf.blit(text_c, (260, 120))
        mouse = pygame.mouse.get_pos()
        if 200+240 > mouse[0] > 200 and 200+50 > mouse[1] > 200:
            pygame.draw.rect(self.surf, bright_green, (200, 200, 240, 50))
        else:
            pygame.draw.rect(self.surf, green, (200, 200, 240, 50))

        start_test = button_font.render("RESUME GAME", 10, black)
        self.surf.blit(start_test, (245, 215))

        if 200+240 > mouse[0] > 200 and 300+50 > mouse[1] > 300:
            pygame.draw.rect(self.surf, bright_red, (200, 300, 240, 50))
        else:
            pygame.draw.rect(self.surf, red, (200, 300, 240, 50))

        start_test = button_font.render("BACK TO MENU", 10, black)
        self.surf.blit(start_test, (245, 315))
        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            return "EXIT"
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 200+240 > mouse[0] > 200 and 200+50 > mouse[1] > 200:
                return "PREV"
            elif 200+240 > mouse[0] > 200 and 300+50 > mouse[1] > 300:
                return "MENU"
        return "NONE"
