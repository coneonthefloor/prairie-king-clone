import os
import pygame
from constants import HEIGHT, WIDTH
from game_object import GameObject
from tilemap import Tilemap


class Ground(GameObject):
    def __init__(self, y_offset):
        super().__init__("ground")
        ground_tile_sheet = pygame.image.load(os.path.join("assets", "sheet.png"))
        tilemap = Tilemap(ground_tile_sheet, (16, 16), 0, 0)
        tilemap.load()

        self.y_offset = y_offset
        self.top_image = tilemap.get_tile_scaled((7, 2), (5, 5))
        self.blank_image = tilemap.get_tile_scaled((11, 1), (5, 5))
        self.variant_image = tilemap.get_tile_scaled((8, 6), (5, 5))
        self.tile_width = self.top_image.get_width()
        self.tile_height = self.top_image.get_height()
        self.tile_count = WIDTH // self.tile_width
        self.full_image = None

    def generate_full_image(self):
        surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        for i in range(0, self.tile_count):
            x_offset = self.tile_width * i
            surface.blit(self.top_image, (x_offset, self.y_offset))
            current_height = self.tile_height
            while self.y_offset + current_height < HEIGHT:
                surface.blit(
                    self.blank_image, (x_offset, self.y_offset + current_height)
                )
                current_height += self.tile_height
        return surface

    def draw(self, surface):
        if not self.full_image:
            self.full_image = self.generate_full_image()
        surface.blit(self.full_image, (0, 0, WIDTH, HEIGHT))
