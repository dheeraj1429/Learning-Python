import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bird_surf_1 = pygame.image.load('./assets/player/bird_1.png').convert_alpha()
        self.bird_surf_2 = pygame.image.load('./assets/player/bird_2.png').convert_alpha()
        self.bird_frame_index = 0
        self.bird_frames = [self.bird_surf_1, self.bird_surf_2]
        self.image = self.bird_frames[self.bird_frame_index]
        self.rotate = 15
        self.image = pygame.transform.rotozoom(self.image, self.rotate, 1)
        self.rect = self.image.get_rect(midbottom=(50,350))
        self.gravity = 0
    
    def jump(self):
        self.gravity = -15
    
    def player_input(self):
        """Handle player inputs like button press events."""
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            self.jump()
            self.fly_animation()
            
        
    def set_image(self):
        self.image = self.bird_frames[self.bird_frame_index]
    
    def fly_animation(self):  
        self.bird_frame_index = 1
        self.set_image()
    
    def flow_down(self):
        self.bird_frame_index = 0
        self.set_image()
        
    def pos_y(self):
        return self.rect.y
    
    def apply_gravity(self):
        """Keeps track the current gravity"""
        self.gravity += 1
        self.rect.y += self.gravity
        self.bird_frame_index = 0
        self.set_image()
        
    def update(self): 
        self.apply_gravity()
        self.player_input()