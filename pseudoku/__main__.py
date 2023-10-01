from .mini3x3 import Mini3x3
from .settings import Settings, load_settings, save_settings
import pygame
from pygame import display


class Pseudoku:
    def __init__(self):
        self.settings = load_settings()
        self.screen = display.set_mode((self.settings.width, self.settings.height))
        self.running = True

    def init(self):
        pygame.init()
        self.settings.theme.load_fonts()

    def run(self):
        self.init()
        self.main_loop()
        self.quit()

    def main_loop(self):
        while self.running:
            self.handle_events()
            self.draw()
            self.update()

        self.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill(self.settings.theme.background_colour.rgb)

    def update(self):
        display.flip()

    def quit(self):
        save_settings(self.settings)
        pygame.quit()


if __name__ == "__main__":
    Pseudoku().run()
