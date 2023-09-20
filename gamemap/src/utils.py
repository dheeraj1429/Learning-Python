import pygame
from csv import reader
from os import walk

def import_csv_file(path):
    level_list = []
    with open(path) as map:
        for row in reader(map, delimiter=','):
            level_list.append(list(row))

    return level_list


def import_cut_graphic(path, tile_size):
    surface = pygame.image.load(path).convert_alpha()

    surface_row = int(surface.get_size()[0] / tile_size)
    surface_column = int(surface.get_size()[1] / tile_size)
    cut_tiles_list = []

    for row in range(surface_row):
        for col in range(surface_column):
            x = col * tile_size
            y = row * tile_size

            # need to create new surface
            new_surface = pygame.Surface((tile_size, tile_size), flags=pygame.SRCALPHA)
            new_surface.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
            cut_tiles_list.append(new_surface)

    return cut_tiles_list


def import_folder(path):
    image_files = []
    for _,_2,file_list in walk(path):
        for file in file_list:
            image_files.append(path + '/' + file)
    
    return image_files