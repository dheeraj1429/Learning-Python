import pygame
from utils import import_folder


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_size, x, y):
        super().__init__()
        self.image = pygame.Surface((tile_size, tile_size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift):
        self.rect.x += shift


class StaticTile(Tile):
    def __init__(self, tile_size, x, y, surface):
        super().__init__(tile_size, x, y)
        self.image = surface
        
        
class Crate(StaticTile):
    def __init__(self, tile_size, x, y, surface):
        super().__init__(tile_size, x, y, pygame.image.load(surface).convert_alpha())
        offset_y = y + tile_size
        self.rect = self.image.get_rect(bottomleft=(x, offset_y))


class Animation(Tile):
    def __init__(self, tile_size, x, y, path):
        super().__init__(tile_size, x, y)
        self.frame_index = 0
        self.image_frames = import_folder(path)

    
    def update(self, shift):
        self.rect.x += shift
        self.frame_index += 0.15
        if self.frame_index >= len(self.image_frames): self.frame_index = 0
        self.image = pygame.image.load(self.image_frames[int(self.frame_index)]).convert_alpha()
    

class Coin(Animation):
    def __init__(self, tile_size, x, y, path):
        super().__init__(tile_size, x, y, path)
        self.image_pos_x = x + tile_size / 2
        self.image_pos_y = y + tile_size / 2
        self.rect = self.image.get_rect(center=(self.image_pos_x, self.image_pos_y))
        

class Tree(Animation):
    def __init__(self, tile_size, x, y, path):
        super().__init__(tile_size, x, y, path)
        offset_y = y - (tile_size / 2)
        self.rect = self.image.get_rect(topleft=(x, offset_y))