import pygame


class CustomCursor:
    def __init__(self, default_image, clicked_image):
        self.default_image = default_image
        self.clicked_image = clicked_image
        self.rect = self.get_image().get_rect()

    def update(self):
        self.rect = self.get_image().get_rect()
        self.rect.center = self.get_pos()

    def draw(self, surface):
        surface.blit(self.get_image(), self.rect)

    def get_image(self):
        if self.pressed():
            return self.clicked_image
        return self.default_image

    def pressed(self):
        return pygame.mouse.get_pressed()[0]

    def get_pos(self):
        return pygame.mouse.get_pos()
