import os
import pygame
from constants import HEIGHT, WIDTH

from game_object import GameObject


class Clouds(GameObject):
    def __init__(self):
        super().__init__("clouds")
        self.speed = 1
        self.image = pygame.image.load(os.path.join("assets", "clouds.png"))
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        self.pos = self.image.get_rect()

    def update(self):
        self.move(left=True)

    def draw(self, surface):
        surface.blit(self.image, self.pos)
        surface.blit(self.image, (self.pos.x + WIDTH, self.pos.y))
