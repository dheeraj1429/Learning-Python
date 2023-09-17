import pygame
import sys
import random
from player import Player
from obstacle import Obstacle

pygame.init()
width = 800
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

ground_y_pos = 300
snail_x_pos = 700
player_gravity = 0
jump_round = False
game_loop = True
game_active = False
opponent_speed = 5
start_time = 0
obstacle_rect_list = []

font = pygame.font.Font('./font/Pixeltype.ttf', 30)
sky_background = pygame.image.load('./graphics/Sky.png').convert()
ground = pygame.image.load('./graphics/ground.png').convert()

# player
player = pygame.sprite.GroupSingle()
player.add(Player())

# obstacle
obstacle_group = pygame.sprite.Group()

# player
player_index = 0

player_walk_1 = pygame.image.load(
    './graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load(
    './graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]

player_jump = pygame.image.load('./graphics/Player/jump.png').convert_alpha()
player_surf = player_walk[player_index]
player_ract = player_surf.get_rect(midbottom=(40, ground_y_pos))

player_stand = pygame.image.load(
    './graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_ract = player_stand.get_rect(center=(400, 200))

# game information
game_name = font.render("Pixel Runner", False, (111, 196, 169))
game_name_ract = game_name.get_rect(center=(400, 80))
enter_game = font.render("Press Enter to start game", False, (111, 196, 169))
enter_game_ract = enter_game.get_rect(center=(400, 330))


# obstacle surface
# snail
snail_surface_1 = pygame.image.load(
    './graphics/snail/snail1.png').convert_alpha()
snail_surface_2 = pygame.image.load(
    './graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_surface_1, snail_surface_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]
snail_ract = snail_surf.get_rect(bottomright=(snail_x_pos, ground_y_pos))

# fly
fly_surface_1 = pygame.image.load('./graphics/Fly/Fly1.png').convert_alpha()
fly_surface_2 = pygame.image.load('./graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_surface_1, fly_surface_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]


# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score = int(current_time / 1000)
    score_surface = font.render(
        f'Score: {score}', False, "Black")
    score_ract = score_surface.get_rect(center=(400, 20))
    screen.blit(score_surface, score_ract)
    return score


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle in obstacle_list:
            obstacle.x -= 5

            if obstacle.bottom == 200:
                screen.blit(fly_surf, obstacle)
            else:
                screen.blit(snail_surf, obstacle)

        obstacle_list = [
            obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []


def collision(player, obstacle):
    if obstacle:
        for obstacle_list in obstacle:
            if player.colliderect(obstacle_list):
                return False
    return True


def player_animation():
    global player_index, player_surf

    if player_ract.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]


while game_loop:
    for event in pygame.event.get():

        # pygame events
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not jump_round:
                    jump_round = True
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_ract.x = 800 + random.randint(1, 500)
                game_active = True
                start_time = pygame.time.get_ticks()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(random.choice(['Fly', "Snail"])))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

    if game_active:
        
        screen.blit(sky_background, (0, 0))
        screen.blit(ground, (0, ground_y_pos))


        obstacle_movement(obstacle_rect_list)
        score = display_score()

        player_gravity += 1
        player_ract.y += player_gravity
        if player_ract.bottom >= ground_y_pos:
            player_ract.bottom = ground_y_pos
            jump_round = False
        player_animation()
        screen.blit(player_surf, player_ract)
        
        # draw player
        player.draw(screen)
        player.update()

        # draw obstacles
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        
        game_active = collision(player_ract, obstacle_rect_list)
    else:
        obstacle_rect_list.clear()
        screen.fill((94, 129, 162))
        screen.blit(game_name, game_name_ract)
        screen.blit(player_stand, player_stand_ract)
        screen.blit(enter_game, enter_game_ract)

    pygame.display.update()
    clock.tick(60)
