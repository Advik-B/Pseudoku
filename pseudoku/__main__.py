import pygame
from pygame import display

from screeninfo import get_monitors
from .classes.settings import Settings, DEFAULT as DEFAULT_SETTINGS
from .pseudoku_grid import SudokuGrid


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
        self.settings = DEFAULT_SETTINGS
        self.monitors = get_monitors()[0]
        self.set_display()
        self.running = True
        self.clock = pygame.time.Clock()
        self.set_caption()
        self.grid_size_divisor = 40
        # self.load_grids()

    def set_display(self):
        self.flags = []
        if self.settings.vsync:
            self.flags.append(pygame.HWSURFACE | pygame.DOUBLEBUF)
        if self.settings.full_screen:
            self.settings.size = (self.monitors.width, self.monitors.height)
            self.flags.append(pygame.FULLSCREEN)
        if self.settings.resizable:
            self.flags.append(pygame.RESIZABLE)

        self.screen = display.set_mode(self.settings.size, or_flags(self.flags))
        self.screen_rect = self.screen.get_rect()

    def load_grids(self):
        # Load the 9 mini 3x3 grids
        self.mini_grids = []

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
        if self.settings.debug:
            print(f"Screen Size: {self.settings.size}")
            print(f"Screen Rect: {self.screen_rect}")
            print(f"Monitors: {self.monitors}")
            self.fps_text = self.settings.theme.psuedoku_font.render(
                f"{self.clock.get_fps():.2f} FPS",
                self.settings.theme.triad_colour,
                antialias=True,
            )
            # Update the FPS text rect to be in the top left corner of the screen
            self.fps_text_rect = self.fps_text.get_rect(topleft=(10, 10))
        minsizex = min(self.screen_rect.width, self.screen_rect.height)

        # Create the grid with default settings and values, this will be changed later by grepos function
        self.grid = SudokuGrid(
            screen=self.screen,
            settings=self.settings,
            x=self.screen_rect.centerx,
            y=self.screen_rect.centery,
            size=(
                minsizex // self.grid_size_divisor,
                minsizex // self.grid_size_divisor,
            ),
        )

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
        if self.settings.debug:
            self.screen.blit(self.fps_text, self.fps_text_rect)
        self.grid.draw()
        pygame.display.flip()
        self.clock.tick(self.settings.fps)

    def update(self):
        # Check if the window has been resized
        if self.settings.resizable and self.settings.size != self.screen.get_size():
            self.resize(self.screen.get_size())

        if (
            self.settings.debug
        ):  # Update the caption if we are in debug mode to show the FPS
            self.set_caption()
            # Update the FPS text
            self.fps_text = self.settings.theme.psuedoku_font.render(
                f"{self.clock.get_fps():.2f} FPS",
                self.settings.theme.background_colour,
                True,
            )

        # Update the grid
        self.grid.update()

    def quit(self):
        pygame.quit()

    def resize(self, size: tuple[int, int]):
        print(f"Resizing to {size}")
        self.settings.resizable = True
        self.settings.size = size
        self.set_display()
        self.grepos()

    def grepos(self):
        minsizex = min(self.screen_rect.width, self.screen_rect.height)
        self.grid.repos(
            self.screen_rect.centerx,
            self.screen_rect.centery,
            size=(
                minsizex // self.grid_size_divisor,
                minsizex // self.grid_size_divisor,
            ),
        )


if __name__ == "__main__":
    Pseudoku().run()
