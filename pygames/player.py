
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.y_pos = 300
        self.gravity = 0
        self.jump_round = False
        self.player_index = 0
        self.player_walk_1 = pygame.image.load('./graphics/Player/player_walk_1.png').convert_alpha()
        self.player_walk_2 = pygame.image.load('./graphics/Player/player_walk_2.png').convert_alpha()
        self.player_jump = pygame.image.load('./graphics/Player/jump.png').convert_alpha()
        self.player_frames = [self.player_walk_1, self.player_walk_2]
        self.image = self.player_frames[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, self.y_pos))
        self.jump_sound = pygame.mixer.Sound('./audio/jump.mp3')
        self.jump_sound.set_volume(0.1)

    def player_input(self):
        """Keep track the player's pressed button"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jump_round:
            self.jump_round = True
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= self.y_pos:
            self.rect.bottom = self.y_pos
            self.jump_round = False
            
    def animation_state(self):
        """Animation of the player"""
        if self.rect.bottom < self.y_pos:self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_frames):self.player_index = 0
            self.image = self.player_frames[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()