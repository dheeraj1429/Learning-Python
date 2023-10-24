import pygame
from settings import GROUND_WIDTH


class Ground(pygame.sprite.Sprite):
    def __init__(self, initial_position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/ground/0.png').convert_alpha()
        self.initial_position = initial_position
        self.rect = self.image.get_rect(topleft=(self.initial_position))
        self.move_speed = 300

    def update(self, dt):
        self.rect.x -= self.move_speed * dt
        if self.rect.x < -(GROUND_WIDTH + 300):
            self.kill()
