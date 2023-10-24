import pygame
from os import walk


def import_folder(path):
    folder_list = []
    for (_, _2, image_folder) in walk(path):
        for image in sorted(image_folder, key=lambda item: item):
            new_surface = pygame.image.load(f'{path}/{image}').convert_alpha()
            folder_list.append(new_surface)
    return folder_list
