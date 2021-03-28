import pygame
import sys

from settings import Settings
from object import Object


class App:
    """Overall class managing game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        # Initialize pygame
        pygame.init()
        # Create settings
        self.settings = Settings()

        # Create screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # Create clock
        self.clock = pygame.time.Clock()
        self.time = 1 / self.settings.FPS
        # Objects list to store Object
        self.objects = []

        pygame.display.set_caption('App')
    
    def run_simulation(self):
        """Run App"""
        while True:
            self._check_events()
            for object in self.objects:
                object.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_events(self):
        """Checks and responds to events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._mouse_press()
    
    def _mouse_press(self):
        """Creates an Object at the position of the mouse press"""
        # Get mouse position
        mouse_coords = pygame.mouse.get_pos()
        x, y = mouse_coords
        # Create an Object and add it to the objects list
        object = Object(self, x, y)
        self.objects.append(object)

    def _update_screen(self):
        """Update images on the screen and flip to a new screen"""
        # Redraw the screen at each pass in the loop
        self.screen.fill(self.settings.screen_bg_color)
        
        # Draw events
        for object in self.objects:
            object.draw()

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    app = App()
    app.run_simulation()
