import pygame
from constants import HEIGHT, WIDTH


class GameObject:
    def __init__(self, tag):
        self.tag = tag
        self.speed = 0
        self.pos = pygame.Rect(0, 0, 0, 0)

    def update(self):
        pass

    def draw(self):
        pass

    def get_image_height(self):
        return self.image.get_height()

    def get_image_width(self):
        return self.image.get_width()

    def move(self, up=False, down=False, left=False, right=False):
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if down:
            self.pos.top += self.speed
        if up:
            self.pos.top -= self.speed

        if self.pos.left >= WIDTH:
            self.pos.right = self.speed
        if self.pos.right <= 0:
            self.pos.left = WIDTH - self.speed

        if self.pos.top >= HEIGHT:
            self.pos.bottom = self.speed
        if self.pos.bottom <= 0:
            self.pos.top = HEIGHT - self.speed
