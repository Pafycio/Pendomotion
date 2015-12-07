import pygame
from state_controller import StateController
__author__ = 'Pawel'


class App():
    """
    MAIN CLASS
    """
    def __init__(self):
        """
        init game
        :return:
        """
        self.running = True
        self._display_surf = None
        self.fps_limit = 60
        self.clock = None
        self._state_controller = None
        self.size = self.weight, self.height = 640, 630

    def on_init(self):
        """
        :return:
        """
        pygame.init()
        pygame.display.set_caption('PendoMotion')
        self.clock = pygame.time.Clock()
        self._display_surf = pygame.display.set_mode(self.size)
        self.running = True
        self._state_controller = StateController(self, self._display_surf)

    @staticmethod
    def on_clean_up():
        """

        :return:
        """
        pygame.quit()

    def on_execute(self):
        """

        :return:
        """
        if self.on_init():
            self.running = False

        while self.running:
            self.clock.tick(self.fps_limit)
            self._state_controller.state_handler()

        self.on_clean_up()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()