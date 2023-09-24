import pygame
from os import walk
from settings import *
from button import Button

def import_folder(path):
    for (_,_2,files) in walk(path):
        return files
    
def load_folder(path):
    images_list = import_folder(path)
    surface_list = []
    for item in images_list:
        new_surface = pygame.image.load(f'{path}/{item}').convert_alpha()
        new_surface = pygame.transform.scale(new_surface, (TILE_SIZE, TILE_SIZE))
        surface_list.append(new_surface)
    return surface_list
