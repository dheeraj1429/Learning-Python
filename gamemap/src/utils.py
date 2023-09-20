from settings import tile_size
import pygame
from csv import reader
from os import walk


def import_csv_file(path):
    terrain_list = []
    with open(path) as map:
        level = reader(map, delimiter=',')
        for row in level:
            terrain_list.append(list(row))
    return terrain_list


def import_cut_graphic(path):
    # load the graphic file
    surface = pygame.image.load(path)

    # calculate the the size of the graphic image, x and y coordinates
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)

    cut_tiles = []

    for row in range(tile_num_x):
        for col in range(tile_num_y):
            x = col * tile_size
            y = row * tile_size
            new_surface = pygame.Surface(
                (tile_size, tile_size), flags=pygame.SRCALPHA)
            new_surface.blit(surface, (0, 0), pygame.Rect(
                x, y, tile_size, tile_size))
            cut_tiles.append(new_surface)

    return cut_tiles


def import_folder(path):
    surface_list = []
    for _, _2, image_files in walk(path):
        for image in image_files:
            full_path = path + '/' + image
            new_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(new_surface)
    return surface_list
