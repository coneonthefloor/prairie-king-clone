import os
import pygame
from constants import FLOOR, GRAVITY
from game_object import GameObject
from particles import Dust
from tilemap import Tilemap


class Player(GameObject):
    def __init__(self):
        super().__init__("player")
        tile_sheet = pygame.image.load(os.path.join("assets", "characters.png"))
        tilemap = Tilemap(tile_sheet, (32, 32), 0, 0)
        tilemap.load()

        self.sprite_scale = (3, 3)

        self.running_frames = [
            tilemap.get_tile_scaled((i, 1), self.sprite_scale) for i in range(14, 18)
        ]

        self.jumping_frames = [
            tilemap.get_tile_scaled((i, 1), self.sprite_scale) for i in range(5, 8)
        ]

        self.dust = []
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
        self.current_frame = 0
        self.jump_force = 20
        self.image = tilemap.get_tile_scaled((0, 1), self.sprite_scale)
        self.speed = 4
        self.grounded = True
        self.vel = pygame.math.Vector2()
        self.initial_pos = pygame.math.Vector2(50, FLOOR)
        self.pos = self.initial_pos.copy()
        self.rect = pygame.Rect(
            *self.pos, self.image.get_width(), self.image.get_height()
        )

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.frame_rate:
            if self.grounded:
                self.current_frame += 1
                if len(self.running_frames) <= self.current_frame:
                    self.current_frame = 0
                self.image = self.running_frames[self.current_frame]
                rect = self.image.get_rect()
                rect.center = self.rect.center
            else:
                if not self.current_frame == len(self.jumping_frames) - 1:
                    self.current_frame += 1
                    self.image = self.jumping_frames[self.current_frame]
                    rect = self.image.get_rect()
                    rect.center = self.rect.center
            self.last_update = current_time

        self.rect.left += self.vel.x
        self.rect.bottom += self.vel.y

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT] and not self.grounded:
            self.vel.x = -self.speed
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            self.vel.x = self.speed
        if pressed[pygame.K_w] or pressed[pygame.K_UP]:
            if self.grounded:
                self.grounded = False
                self.current_frame = 0
                self.vel.y = -self.jump_force
        if (
            not pressed[pygame.K_a]
            and not pressed[pygame.K_LEFT]
            and not pressed[pygame.K_d]
            and not pressed[pygame.K_RIGHT]
            and not pressed[pygame.K_w]
            and not pressed[pygame.K_UP]
            and self.grounded
        ):
            self.vel.x = 0

        if self.rect.bottom < FLOOR:
            self.vel.y += GRAVITY
        if self.rect.bottom > FLOOR:
            if not self.grounded:
                if self.vel.x < 0:
                    self.dust.append(Dust(self.rect.bottomleft))
                else:
                    self.dust.append(Dust(self.rect.midbottom))
                self.vel.x = 0
                self.current_frame = 0
                self.dust = list(filter(lambda x: len(x.particles) != 0, self.dust))
            self.grounded = True
            self.rect.bottom = FLOOR

        if self.vel.x == 0 and self.rect.left > self.initial_pos.x and self.grounded:
            self.rect.move_ip(-self.speed, 0)
        if self.vel.x < self.speed:
            self.frame_rate = 200
        else:
            self.frame_rate = 100
        if self.rect.left < self.initial_pos.x:
            self.rect.left = self.initial_pos.x

    def draw(self, surface):
        for i in range(len(self.dust)):
            if len(self.dust[i].particles) > 0:
                self.dust[i].draw(surface)
                self.dust[i].update()
        surface.blit(self.image, self.rect)
