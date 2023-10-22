class Monster:
    def __init__(self, health, energy, **kwargs):
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)

        # private attributes
        self._has_move = False

    def attack(self, amount):
        self.health -= amount
        print(f"{self.health} health loss")


class Fish:
    def __init__(self, speed, has_scales, **kwargs):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)

    def swim(self):
        print('you can also swim')


class Shark(Monster, Fish):
    def __init__(self, health, energy, speed, has_scales):
        super().__init__(health=health, energy=energy, speed=speed, has_scales=has_scales)


shark = Shark(health=20, energy=30, speed=200, has_scales=True)
# print(hasattr(shark, 'speed'))
# print(hasattr(shark, 'some_attr'))
# setattr(shark, 'weapon', 'Sword')
# print(shark.weapon)
