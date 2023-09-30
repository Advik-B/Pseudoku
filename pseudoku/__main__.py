import pygame

pygame.init()
pygame.font.init()

from .mini3x3 import Mini3x3
from .settings import Settings, load_settings, save_settings


settings: Settings = load_settings()

screen = pygame.display.set_mode((settings.width, settings.height))
pygame.display.set_caption("Pseudoku")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            save_settings(settings)
            exit()
    screen.fill(settings.theme.background_colour.rgb)
    pygame.display.update()
