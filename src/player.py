import os
import pygame
from constants import FLOOR, GRAVITY
from game_object import GameObject
from tilemap import Tilemap


class Player(GameObject):
    def __init__(self):
        super().__init__("player")
        tile_sheet = pygame.image.load(os.path.join("assets", "characters.png"))
        tilemap = Tilemap(tile_sheet, (32, 32), 0, 0)
        tilemap.load()

        self.jump_force = 20
        self.image = tilemap.get_tile_scaled((0, 1), (2.5, 2.5))
        self.speed = 4
        self.grounded = True
        self.vel = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(50, FLOOR)
        self.rect = pygame.Rect(
            *self.pos, self.image.get_width(), self.image.get_height()
        )

    def update(self):
        self.rect.left += self.vel.x
        self.rect.bottom += self.vel.y

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            self.vel.x = -self.speed
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            self.vel.x = self.speed
        if pressed[pygame.K_w] or pressed[pygame.K_UP]:
            if self.grounded:
                self.grounded = False
                self.vel.y = -self.jump_force

        if self.rect.bottom < FLOOR:
            self.vel.y += GRAVITY
        if self.rect.bottom > FLOOR:
            self.grounded = True
            self.rect.bottom = FLOOR

    def draw(self, surface):
        surface.blit(self.image, self.rect)
