import pygame
from pygame.locals import *

class App:
    def __init__(self):
        # Function will create our game loop
        self._running = True
        self._dispaly_surf = None   # Display surface
        self.size = 640
        self.height = 400

    def on_init(self):
        pygame.init()
        self._dispaly_surf = pygame.display.set_mode((self.size, self.height))
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

        self.on_cleanup()
    
if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
