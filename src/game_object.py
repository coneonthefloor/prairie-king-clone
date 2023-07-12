import pygame
from constants import HEIGHT, WIDTH


class GameObject:
    def __init__(self, tag):
        self.tag = tag
        self.speed = 0
        self.width = 0
        self.height = 0
        self.pos = pygame.Vector2()

    def update(self):
        pass

    def draw(self):
        pass

    def move(self, up=False, down=False, left=False, right=False):
        if right:
            self.pos.x += self.speed
        if left:
            self.pos.x -= self.speed
        if down:
            self.pos.y += self.speed
        if up:
            self.pos.y -= self.speed

        if self.pos.x >= WIDTH:
            self.pos.x = self.speed + self.width
        if self.pos.x + self.width <= 0:
            self.pos.x = WIDTH - self.speed

        if self.pos.y >= HEIGHT:
            self.pos.y = self.speed + self.height
        if self.pos.y + self.height <= 0:
            self.pos.y = HEIGHT - self.speed
