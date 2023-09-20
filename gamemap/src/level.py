import pygame
from settings import tile_size
from utils import import_csv_file, import_cut_graphic
from tile import StaticTile, Coin, Tree


class Level():
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.shift_world = 0

        # tiles
        tiles_layout = import_csv_file(level_data["terrain"])
        self.tile_sprite_list = import_cut_graphic('../public/graphics/terrain/terrain_tiles.png', tile_size)
        self.tiles_sprite_layout = self.create_sprite_group(tiles_layout, "terrain")

        # grass
        grass_layout = import_csv_file(level_data["grass"])
        self.grass_sprite_list = import_cut_graphic('../public/graphics/decoration/grass/grass.png', tile_size)
        self.grass_sprite_layout = self.create_sprite_group(grass_layout, 'grass')

        # coins
        coin_layout = import_csv_file(level_data["coins"])
        self.coin_sprite_layout = self.create_sprite_group(coin_layout, 'coins')
        
        # trees
        tree_layout = import_csv_file(level_data["fg palms"])
        self.tree_sprite_layout = self.create_sprite_group(tree_layout, 'tree')

    def create_sprite_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for column_index, value in enumerate(row):
                if value != '-1':
                    # get the x and y coordinates of the column.
                    x = column_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        single_sprite = self.tile_sprite_list[int(value)]
                        tile = StaticTile(tile_size, x, y, single_sprite)
                        sprite_group.add(tile)


                    if type == 'grass':
                        single_sprite = self.grass_sprite_list[int(value)]
                        grass = StaticTile(tile_size, x, y, single_sprite)
                        sprite_group.add(grass)


                    if type == 'coins':
                        coin_sprite = Coin(tile_size, x, y, '../public/graphics/coins/gold' if value == '0' else "../public/graphics/coins/silver")
                        sprite_group.add(coin_sprite)
                        
                    
                    if type == 'tree':
                        tree_sprite = Tree(tile_size, x, y, '../public/graphics/terrain/palm_small')
                        sprite_group.add(tree_sprite)

        return sprite_group

    def run(self):

        # tile
        self.tiles_sprite_layout.draw(self.display_surface)
        self.tiles_sprite_layout.update(self.shift_world)

        # grass
        self.grass_sprite_layout.draw(self.display_surface)
        self.grass_sprite_layout.update(self.shift_world)
        
        # coins
        self.coin_sprite_layout.draw(self.display_surface)
        self.coin_sprite_layout.update(self.shift_world)
        
        # trees
        self.tree_sprite_layout.draw(self.display_surface)
        self.tree_sprite_layout.update(self.shift_world)
