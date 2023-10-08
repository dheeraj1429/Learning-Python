import pygame
from settings import *
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.import_assets()
        
        self.image = pygame.Surface((64, 32))
        self.speed = 200
        self.status = 'down'
        self.frame_index = 0
        
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        
        self.movement = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        
        
    def import_assets(self):
        self.animations = {
            'up': [],'down': [],'left': [], 'right': [],
            'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
            'right_hoe': [], 'left_hoe': [], 'up_hoe': [], 'down_hoe': [],
            'right_axe': [], 'left_axe': [], 'up_axe': [], 'down_axe': [],
            'right_water': [], 'left_water': [], 'up_water': [], 'down_water': [],
        }
        
        for animation in self.animations.keys():
            path = '../graphics/character' + '/' + animation
            self.animations[animation] = import_folder(path)
        
    def get_status(self):
        if self.movement.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'
        
    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.movement.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.status = 'down'
            self.movement.y = 1
        else:
            self.movement.y = 0
        
        if keys[pygame.K_RIGHT]:
            self.movement.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.movement.x = -1
            self.status = 'left'
        else:
            self.movement.x = 0
            
            
    def move(self, dt):

        if self.movement.magnitude() > 0:
            self.movement = self.movement.normalize()
            
        self.pos.x += self.movement.x * self.speed * dt
        self.rect.centerx = self.pos.x
        
        self.pos.y += self.movement.y * self.speed * dt
        self.rect.centery = self.pos.y
        
    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]
        
    def update(self, dt):
        self.input()
        self.get_status()
        self.move(dt)
        self.animate(dt)