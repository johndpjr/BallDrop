import pygame
from random import randint


class Object:
    """Models an object in the simulation"""

    def __init__(self, engine, x, y):
        """Create an object initially at position (x, y)"""
        self.engine = engine
        self.x = x
        self.y = y

        # Assume the object to be falling initially
        self.ay = self.engine.settings.GRAVITATIONAL_CONSTANT

        # The object has no initial velocity
        self.vx = randint(100, 1000) * randint(-1, 1)
        self.vy = 0

        # Draw object
        self.circle = pygame.draw.circle(self.engine.screen, (0, 0, 0), (self.x, self.y), 5)

        # Screen rect
        self.screen_rect = self.engine.screen.get_rect()

        self.at2 = 0.5 * self.ay * self.engine.time**2
    
    def update(self):
        # Update every 1 / FPS (dt)
        t = self.engine.time
        self._check_all_collisions()

        # Updating position
        # dx = v0t + 1/2at^2
        self.x += self.vx * t
        self.y += self.vy * t + self.at2

        # Updating velocity
        # v = v0 + at
        self.old_vx = self.vx
        self.old_vy = self.vy

        self.vy += self.ay*t
        

    def draw(self):
        self.circle = pygame.draw.circle(self.engine.screen, (0, 0, 0), (self.x, self.y), 5)
    
    def _check_all_collisions(self):
        """Checks and responds to all collisions"""
        # Object hits the bottom; reduce and reverse the velocity
        self._check_bottom_collision()
        self._check_side_collision()
    
    def _check_bottom_collision(self):
        """Checks and responds to collisions with the bottom"""
        if self.circle.bottom >= self.screen_rect.bottom:
            if self.vy > 0:
                # Reverse and reduce the velocity
                self.vy *= -1
                self.vy *= self.engine.settings.ELASTIC_CONSTANT

                if abs(self.old_vy - self.vy) < 1:
                    self.engine.objects.remove(self)
    
    def _check_side_collision(self):
        """Checks and responds to collisions with the sides"""
        if self.circle.left <= self.screen_rect.left or self.circle.right >= self.screen_rect.right:
            # Reverse the x velocity
            self.vx *= -1
            self.vx *= self.engine.settings.ELASTIC_CONSTANT
            if abs(self.old_vx - self.vx) < 1:
                self.vx = 0