import pygame
from os import walk


def import_folders(path):
    images_surface_list = []
    for (_, _2, images_list) in walk(path):
        for image in images_list:
            image_surface = pygame.image.load(f'{path}/{image}').convert_alpha()
            images_surface_list.append(image_surface)
    return images_surface_list
