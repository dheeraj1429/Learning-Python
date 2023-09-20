import pygame
from utils import import_csv_file, import_cut_graphic
from settings import tile_size
from tile import StaticTile, Crate, Coin, Plam
from enemies import Enemies


class Level():
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.shift_world = 0

        # terrain setup
        terrain_layout = import_csv_file(level_data['terrain'])
        self.terrain_sprite = self.create_tile_group(terrain_layout, 'terrain')

        # grass setup
        grass_layout = import_csv_file(level_data['grass'])
        self.grass_sprite = self.create_tile_group(grass_layout, 'grass')

        # crate setup
        crate_layout = import_csv_file(level_data['crates'])
        self.crate_sprite = self.create_tile_group(crate_layout, 'crates')

        # coins setup
        coin_layout = import_csv_file(level_data['coins'])
        self.coin_sprite = self.create_tile_group(coin_layout, 'coins')

        # palms tress setup
        fg_palm_tree_layout = import_csv_file(level_data['fg palms'])
        self.fg_palm_tree_sprite = self.create_tile_group(
            fg_palm_tree_layout, 'fg palms')

        # anemies
        enemies_layout = import_csv_file(level_data["enemies"])
        self.enemies_sprite = self.create_tile_group(enemies_layout, 'enemies')

    def create_tile_group(self, layout, type):
        # create a sprite group
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for column_index, value in enumerate(row):
                if value != '-1':
                    x = column_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphic(
                            '../public/graphics/terrain/terrain_tiles.png')
                        single_tile = terrain_tile_list[int(value)]
                        sprite = StaticTile(tile_size, x, y, single_tile)

                    if type == 'grass':
                        grass_tile_list = import_cut_graphic(
                            '../public/graphics/decoration/grass/grass.png')
                        single_tile = grass_tile_list[int(value)]
                        sprite = StaticTile(tile_size, x, y, single_tile)

                    if type == 'crates':
                        sprite = Crate(tile_size, x, y)

                    if type == 'coins':
                        path = '../public/graphics/coins/'
                        if value == '0':
                            path += '/gold'
                        else:
                            path += '/silver'
                        sprite = Coin(
                            tile_size, x, y, path)

                    if type == 'fg palms':
                        if value == '0':
                            sprite = Plam(tile_size, x, y,
                                          '../public/graphics/terrain/palm_small', 38)
                        else:
                            sprite = Plam(tile_size, x, y,
                                          '../public/graphics/terrain/palm_large', 64)

                    if type == 'enemies':
                        sprite = Enemies(
                            tile_size, x, y, '../public/graphics/enemy/run')

                    sprite_group.add(sprite)

        return sprite_group

    def run(self):
        # terrain
        self.terrain_sprite.draw(self.display_surface)
        self.terrain_sprite.update(self.shift_world)

        # crate
        self.crate_sprite.draw(self.display_surface)
        self.crate_sprite.update(self.shift_world)

        # grass
        self.grass_sprite.draw(self.display_surface)
        self.grass_sprite.update(self.shift_world)

        # coins
        self.coin_sprite.draw(self.display_surface)
        self.coin_sprite.update(self.shift_world)

        # enemies
        self.enemies_sprite.draw(self.display_surface)
        self.enemies_sprite.update(self.shift_world)

        # plam trees
        self.fg_palm_tree_sprite.draw(self.display_surface)
        self.fg_palm_tree_sprite.update(self.shift_world)
