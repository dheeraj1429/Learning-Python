import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        # positions
        self.obstacle_1_pos_y = random.randint(900, 1200)
        self.obstacle_2_pos_y = random.randint(400, 500)
        self.pos_y = self.obstacle_1_pos_y
        self.move_x_speed = 5
        
        self.obstacle = pygame.image.load(f'./assets/obstacle/pillar/{type}.png').convert_alpha()
        self.image = self.obstacle
        
        if type == 'pillar_2':
            self.pos_y = self.obstacle_2_pos_y
        else:
            self.pos_y = self.obstacle_1_pos_y
            
        self.rect = self.image.get_rect(midbottom=(500 + random.randint(100, 200),self.pos_y))
        
    def move_x(self):
        self.rect.x -= self.move_x_speed
    
    def distory(self):
        """remove the obstacles class"""
        if self.rect.x <= -100:
            self.kill()
            
    def update(self):
        self.move_x()
        self.distory()