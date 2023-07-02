import pygame


class Tilemap:
    def __init__(self, image_path, tile_size, margin, spacing):
        self.tiles = []
        self.margin = margin
        self.spacing = spacing
        self.tile_size = tile_size
        self.image_path = image_path
        self.image = pygame.image.load(self.image_path)
        self.image_rect = self.image.get_rect()

    def load(self):
        width = self.image_rect.width
        height = self.image_rect.height
        for col in range(self.margin, width, self.tile_size[0] + self.spacing):
            current_row = []
            for row in range(self.margin, height, self.tile_size[1] + self.spacing):
                tile = pygame.Surface(self.tile_size)
                tile.blit(self.image, (0, 0), (col, row, *self.tile_size))
                current_row.append(tile)
            self.tiles.append(current_row)

    def get_tile(self, tile):
        return self.tiles[tile[0]][tile[1]]
