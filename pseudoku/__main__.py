from .mini3x3 import Mini3x3
from .settings import Settings, load_settings, save_settings
from screeninfo import get_monitors
import pygame
from pygame import display


def or_flags(flags: list[int]) -> int:
    """
    OR all the pygame flags together
    :param flags:  List of pygame flags
    :return:       OR'd flags
    """
    result = flags[0]
    flags = flags[1:]
    for flag in flags:
        result |= flag
    return result


class Pseudoku:
    def __init__(self):
        self.settings = load_settings()
        self.monitors = get_monitors()[0]
        flags = []
        if self.settings.vsync:
            flags.append(pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED)
        if self.settings.full_screen:
            self.settings.size = (self.monitors.width, self.monitors.height)
            flags.append(pygame.FULLSCREEN)
        if self.settings.resizable:
            flags.append(pygame.RESIZABLE)
        self.screen = display.set_mode(self.settings.size, or_flags(flags))

        self.screen_rect = self.screen.get_rect()

        self.running = True
        self.clock = pygame.time.Clock()
        self.set_caption()
        self.load_grids()

    def load_grids(self):
        # Load the 9 mini 3x3 grids
        self.mini_grids = []
        for i in range(3):
            for j in range(3):
                self.mini_grids.append(
                    Mini3x3(
                        self.settings,
                        self.screen_rect.width // 3 * j,
                        self.screen_rect.height // 3 * i,
                        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                    )
                )

    def set_caption(self):
        if self.settings.debug:
            display.set_caption(
                f"Pseudoku {self.settings.version_string} (DEBUG) - {self.clock.get_fps():.2f} FPS | By: Advik"
            )
        else:
            display.set_caption(f"Pseudoku {self.settings.version_string} | By: Advik")

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
        for grid in self.mini_grids:
            grid.draw()
            self.screen.blit(grid.image, grid.rect)

    def update(self):
        if (
            self.settings.debug
        ):  # Update the caption if we are in debug mode to show the FPS
            self.set_caption()
        pygame.display.flip()
        self.clock.tick(self.settings.fps)

    def quit(self):
        save_settings(self.settings)
        pygame.quit()


if __name__ == "__main__":
    Pseudoku().run()
