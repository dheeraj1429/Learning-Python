import pygame
import sys
from background import Background
from player import Player
from obstacle import Obstacle
import random
from score import Score

game_loop = True
game_active = False

# Game and screen setup
pygame.init()
pygame.display.set_caption("Flappy Game")
screen = pygame.display.set_mode((500, 700))
clock = pygame.time.Clock()


# game heading
game_font_1 = pygame.font.Font('./assets/font/FlappybirdyRegular-KaBW.ttf', 100)
game_font_2 = pygame.font.Font("./assets/font/Blomberg-8MKKZ.otf", 30)

game_heading = game_font_1.render('Flappy Bird', False, "White")
game_heading_rect = game_heading.get_rect(center=(250, 200))

game_background_surf = pygame.image.load('./assets/background/night.png').convert_alpha()
game_background_surf = pygame.transform.rotozoom(game_background_surf, False, 1.1)
game_background_rect = game_background_surf.get_rect(center=(200,300))

play_heading = game_font_2.render('Press space to play', False, "Green")
play_heading_rect = play_heading.get_rect(center=(250, 500))

# background initialization
background = pygame.sprite.GroupSingle()
background.add(Background())

# Player initialization
player = pygame.sprite.GroupSingle()
player.add(Player())

# Obstacles initialization
obstacle_group = pygame.sprite.Group()

# Scoreboard initialization
score = Score()

# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1000)

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    return True

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_active:
            game_active = True
            score.start_time = pygame.time.get_ticks()
            
        if event.type == obstacle_timer:
            obstacle_group.add(Obstacle(random.choice(['pillar_1', 'pillar_2', 'pillar_3', 'pillar_4'])))
            
    if game_active:
        # draw game background
        background.draw(screen)
        
        # player
        player.draw(screen)
        player.update()
        
        # if player.sprite.pos_y() >= 700:
        #     game_active = False
        #     print(game_active)
        
        # obstacle
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        # collision
        game_active = collision_sprite()
        
        # Score draw
        screen.blit(score.heading, score.rect)
        game_score = score.update_score() 
    else:
        screen.blit(game_background_surf, game_background_rect)
        screen.blit(play_heading, play_heading_rect)
        screen.blit(game_heading, game_heading_rect)
    
    pygame.display.update()
    clock.tick(60)