import os
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

columns = 16
rows = 10
margin = 1
spacing = 1
tile_size = 8
tilemap_image = pygame.image.load(os.path.join("assets", "colored_tilemap.png"))
tilemap_image_rect = tilemap_image.get_rect()
tilemap_width = tilemap_image_rect.width
tilemap_height = tilemap_image_rect.height
tiles = []
for col in range(margin, tilemap_width, columns + spacing):
    for row in range(margin, tilemap_height, rows + spacing):
        tile = pygame.Surface((tile_size, tile_size))
        tile.blit(tilemap_image, (0, 0), (col, row, *(tile_size, tile_size)))
        tiles.append(tile)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # RENDER YOUR GAME HERE
    screen.blit(tiles[0], (screen.get_width() / 2, screen.get_height() / 2))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
