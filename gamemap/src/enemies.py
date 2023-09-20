from tile import AnimatedTile


class Enemies(AnimatedTile):
    def __init__(self, tile_size, x, y, path):
        super().__init__(tile_size, x, y, path)
        self.rect.y += tile_size - self.image.get_size()[1]
        self.speed = 2

    def move(self):
        self.rect.x += self.speed
