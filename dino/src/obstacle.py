import pygame
from random import choice
from utils import import_folder


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, initial_position, groups):
        super().__init__(groups)
        self.initial_position = initial_position
        self.move_speed = 300
        self.can_move = False

        # frames
        self.frames = import_folder('../graphics/obstacle/trees')
        self.image = choice(self.frames)
        self.rect = self.image.get_rect(midbottom=initial_position)

    def update(self, dt):
        if self.can_move:
            self.rect.x -= self.move_speed * dt
            if self.rect.x < -100:
                self.kill()
