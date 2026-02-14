import pygame
import sys
from pygame.locals import *
import random

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
DISPLAY_TITLE = "Game"

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("orange_wizard.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("blue_wizard.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
            
        if self.rect.right > SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    


class App:
    def __init__(self):
        # Function will create our game loop
        self._running = True
        self._dispaly_surface = None   # Display surface
        self._display_title = None
        self._fps = FPS
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.player_one = None
        self.enemy_one = None

    @property
    def running(self):
        return self._running
    
    @running.setter
    def running(self, value):
        self._running = value

    @property
    def display_surface(self):
        return self._dispaly_surface
    
    @display_surface.setter
    def display_surface(self, value):
        self._dispaly_surface = value

    @property
    def display_title(self):
        return self._display_title
    
    @display_title.setter
    def display_title(self, value):
        self._display_title = value

    @property
    def fps(self):
        return self._fps
    
    @fps.setter
    def fps(self, value):
        self._fps = value

    def on_init(self):
        pygame.init()
        self._set_display_surface()
        self._set_fps()
        self._set_display_title()
        self._set_running()
        self._create_player()
        self._create_enemy()


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        self.player_one.update()

    def on_loop(self):
        self.enemy_one.move()

        self.dispaly_surface.fill(WHITE)
        self.player_one.draw(self.dispaly_surface)
        self.enemy_one.draw(self.dispaly_surface)

    def on_render(self):
        pygame.display.update()
        self._set_fps()

    def on_cleanup(self):
        pygame.quit()
        sys.exit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

        self.on_cleanup()

    def _set_fps(self):
        FramesPerSecond = pygame.time.Clock()
        FramesPerSecond.tick(self.fps)
    
    def _set_display_surface(self):
        self.dispaly_surface = pygame.display.set_mode(
            (self.width, self.height)
        )

    def _set_running(self):
        self.running = True
    
    def _set_display_title(self):
        self.display_title = DISPLAY_TITLE

    def _create_player(self):
        self.player_one = Player()

    def _create_enemy(self):
        self.enemy_one = Enemy()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
