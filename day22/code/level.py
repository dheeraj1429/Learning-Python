import pygame
from settings import *
from player import Player


class Level:
    def __init__(self):
        # display surface
        self.player = None
        self.display_surface = pygame.display.get_surface()
        
        # sprite group
        self.all_sprite = pygame.sprite.Group()
        
        self.setup()
        
    def setup(self):
        self.player = Player((320, 200), self.all_sprite)
    
    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprite.draw(self.display_surface)
        self.all_sprite.update(dt)