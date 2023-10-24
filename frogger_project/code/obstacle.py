import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, surface, initial_position, groups):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft=initial_position)
