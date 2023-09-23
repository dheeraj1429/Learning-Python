from typing import Any
import pygame
from utils import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, surface):
        super().__init__()
        self.move_speed = 5
        self.direction_x = 0
        self.facing_right = True
        self.gravity = 0
        self.animation_frame_speed = 0.10
        self.display_surface = surface
        self.direction = pygame.math.Vector2(0, 0)
        
        self.run_frames = import_folder('../public/graphics/character/run')
        self.run_frame_index = 0
        self.rest_frames = import_folder('../public/graphics/character/idle')
        self.rest_animation_index = 0
        
        self.image = pygame.image.load(self.rest_frames[int(self.rest_animation_index)]).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x, y))
        
    def rest_animation(self):
        self.rest_animation_index += self.animation_frame_speed
        if self.rest_animation_index >= len(self.rest_frames): self.rest_animation_index = 0
        self.image = pygame.image.load(self.rest_frames[int(self.rest_animation_index)]).convert_alpha()
    
    def move_animation(self):
        self.run_frame_index += self.animation_frame_speed
        if self.run_frame_index >= len(self.run_frames): self.run_frame_index = 0
        self.image = pygame.image.load(self.run_frames[int(self.run_frame_index)]).convert_alpha()
        
            
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
    
    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction_x = self.move_speed
            self.rect.x += self.direction_x
            self.facing_right = True
            self.move_animation()
            # self.flip_animation()
        elif keys[pygame.K_LEFT]:
            self.direction_x = -self.move_speed
            self.rect.x += self.direction_x
            self.facing_right = False
            self.move_animation()
            # self.flip_animation()
        else:
            self.rest_animation()
    
    def update(self):
        self.input()