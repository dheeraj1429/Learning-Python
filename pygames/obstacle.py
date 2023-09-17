import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.obstacle_type = type
        self.obstacle_frames = []
        self.obstacle_index = 0
        self.animation_index = 0
        self.obstacle_speed = 5
        
        if type == "Fly":
            self.fly_surf_1 = pygame.image.load('./graphics/Fly/Fly1.png').convert_alpha()
            self.fly_surf_2 = pygame.image.load('./graphics/Fly/Fly2.png').convert_alpha()
            self.obstacle_frames = [self.fly_surf_1, self.fly_surf_2]
            self.y_pos = 200
        else:
            self.snail_surf_1 = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
            self.snail_surf_2 = pygame.image.load('./graphics/snail/snail2.png').convert_alpha()
            self.obstacle_frames = [self.snail_surf_1, self.snail_surf_2]
            self.y_pos = 300
            
        self.image = self.obstacle_frames[self.obstacle_index]
        self.rect = self.image.get_rect(bottomright=(random.randint(900, 1100), self.y_pos))
        
    def animation_state(self):
        self.animation_index += 1
        if self.animation_index >= len(self.obstacle_frames): self.animation_index = 0
        self.image = self.obstacle_frames[int(self.animation_index)]
        
    def update(self):
        self.rect.x -= self.obstacle_speed
        self.animation_state()
        self.distroy()
        
    def distroy(self):
        """Remove the obstacle from the sheet"""
        if self.rect.x <= -100:
            self.kill()