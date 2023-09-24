import csv
from os import walk
import pygame
from sys import exit
pygame.init()
from button import Button

clock = pygame.time.Clock()

# game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

# variables
ROWS = 16
MAX_COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
CURRENT_TILE = 0

scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1
button_col = 0
button_row = 0


# screen initialization
screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption("Level editor")

# load images
pine_1 = pygame.image.load('./img/Background/pine1.png').convert_alpha()
pine_2 = pygame.image.load('./img/Background/pine2.png').convert_alpha()
mountain = pygame.image.load('./img/Background/mountain.png').convert_alpha()
sky_cloud = pygame.image.load('./img/Background/sky_cloud.png').convert_alpha()
save_image = pygame.image.load('./img/save_btn.png').convert_alpha()


# load folder
def import_folder(path):
    for (_, _2, files) in walk(path):
        return files


# tiles
tiles = import_folder('./img/tile')
tile_list = []
button_list = []
save_button = Button(TILE_SIZE + 20, SCREEN_HEIGHT + 20, save_image, 1)


for tile in range(len(tiles)):
    new_surf = pygame.image.load(f"./img/tile/{tile}.png").convert_alpha()
    new_surf = pygame.transform.scale(new_surf, (TILE_SIZE, TILE_SIZE))
    tile_list.append(new_surf)

for image in range(len(tile_list)):
    button = Button(SCREEN_WIDTH + (75 * button_col) + 50, (75 * button_row) + 50, tile_list[image], 1)
    button_list.append(button)
    
    # create a 3 row of grid
    button_col += 1
    if button_col >= 3:
        button_col = 0
        button_row += 1
        
# world coordinates data
world_data = []

for row in range(ROWS):
    row_list = [-1] * MAX_COLS
    world_data.append(row_list)

for tile in range(0, MAX_COLS):
    world_data[len(world_data) - 1][tile] = 0

# Draw a grid
def draw_grid():
    for col in range(MAX_COLS + 1):
        x = col * TILE_SIZE - scroll
        pygame.draw.line(screen, 'white', (x, 0), (x, SCREEN_HEIGHT))
    for row in range(ROWS + 1):
        y = row * TILE_SIZE
        pygame.draw.line(screen, 'white', (0, y), (SCREEN_WIDTH, y))


# draw background
def draw_bg():
    next_x_pos = sky_cloud.get_width()
    for x in range(6):
        screen.blit(sky_cloud, ((x * next_x_pos) - scroll * 0.5, 0))
        screen.blit(mountain, ((x * next_x_pos) - scroll * 0.6, SCREEN_HEIGHT - mountain.get_height() - 300))
        screen.blit(pine_1, ((x * next_x_pos) - scroll * 0.7, SCREEN_HEIGHT - pine_1.get_height() - 150))
        screen.blit(pine_2, ((x * next_x_pos) - scroll * 0.8, SCREEN_HEIGHT - pine_2.get_height()))


# draw world
def draw_world():
    for row_index, row in enumerate(world_data):
        for col_index, value in enumerate(row):
            if value >= 0:
                x = (col_index * TILE_SIZE - scroll)
                y = (row_index * TILE_SIZE)
                screen.blit(tile_list[value], (x, y))
        
def export_world():
    with open('level.csv', 'w', newline='') as level:
        writer = csv.writer(level)
        writer.writerows(world_data)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            if event.key == pygame.K_SPACE:
                scroll_speed = 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_SPACE:
                scroll_speed = 1

    if scroll_left and scroll > 0:
        scroll -= 5 * scroll_speed
    elif scroll_right and scroll < sky_cloud.get_width() * 5:
        scroll += 5 * scroll_speed
        
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos_x = (mouse_pos[0] + scroll) // TILE_SIZE
    mouse_pos_y = (mouse_pos[1] + scroll) // TILE_SIZE
    
    
    if mouse_pos[0] < SCREEN_WIDTH and mouse_pos[1] < SCREEN_HEIGHT and pygame.mouse.get_pressed()[0]:
        if world_data[mouse_pos_y][mouse_pos_x] != CURRENT_TILE:
            world_data[mouse_pos_y][mouse_pos_x] = CURRENT_TILE
    
    if pygame.mouse.get_pressed()[2]:
        world_data[mouse_pos_y][mouse_pos_x] = -1

    draw_bg()
    draw_grid()
    draw_world()

    pygame.draw.rect(screen, 'green', (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))
    pygame.draw.rect(screen, 'green', (0, SCREEN_HEIGHT, SCREEN_WIDTH + SIDE_MARGIN, LOWER_MARGIN))
    
    for button_index, button in enumerate(button_list):
        if button.draw(screen):
            CURRENT_TILE = button_index
            
    if save_button.draw(screen):
        export_world()
        
    pygame.draw.rect(screen, 'red', button_list[CURRENT_TILE].rect, 4)
    pygame.display.update()
    clock.tick(60)