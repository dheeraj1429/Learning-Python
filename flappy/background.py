import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./assets/background/day.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 1.1)
        self.rect = self.image.get_rect(center=(200,300))