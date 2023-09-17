import pygame
import sys
import random
from player import Player
from obstacle import Obstacle

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

game_loop = True
game_active = False
start_time = 0

# Font
font = pygame.font.Font('./font/Pixeltype.ttf', 30)

# Background
sky_background = pygame.image.load('./graphics/Sky.png').convert()
ground = pygame.image.load('./graphics/ground.png').convert()

# player
player = pygame.sprite.GroupSingle()
player.add(Player())

# obstacle
obstacle_group = pygame.sprite.Group()

# Game sound
game_bg = pygame.mixer.Sound('./audio/music.wav')
game_bg.play()
game_bg.set_volume(0.1)

# player
player_stand = pygame.image.load(
    './graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_ract = player_stand.get_rect(center=(400, 200))

# game information
game_name = font.render("Pixel Runner", False, (111, 196, 169))
game_name_ract = game_name.get_rect(center=(400, 80))
enter_game = font.render("Press Enter to start game", False, (111, 196, 169))
enter_game_ract = enter_game.get_rect(center=(400, 330))


# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score = int(current_time / 1000)
    score_surface = font.render(
        f'Score: {score}', False, "Black")
    score_ract = score_surface.get_rect(center=(400, 20))
    screen.blit(score_surface, score_ract)
    return score


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False): 
        obstacle_group.empty()
        return False
    else: return True

while game_loop:
    for event in pygame.event.get():

        # pygame events
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_active:
            game_active = True
            start_time = pygame.time.get_ticks()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(random.choice(['Fly', "Snail"])))

    if game_active:
        # background
        screen.blit(sky_background, (0, 0))
        screen.blit(ground, (0, 300))

        # Score
        score = display_score()
        
        # draw player
        player.draw(screen)
        player.update()

        # draw obstacles
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        # Keep track of obstacles and player collisions
        game_active = collision_sprite()
    else:
        screen.fill((94, 129, 162))
        screen.blit(game_name, game_name_ract)
        screen.blit(player_stand, player_stand_ract)
        screen.blit(enter_game, enter_game_ract)

    pygame.display.update()
    clock.tick(60)