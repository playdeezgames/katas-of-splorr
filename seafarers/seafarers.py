import math


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 0
        self.speed = 1

    def set_heading(self, new_heading):
        self.heading = new_heading % 32

    def turn(self, delta_heading):
        self.set_heading(self.heading + delta_heading)

    def set_speed(self, new_speed):
        self.speed = max(0, min(1, new_speed))

    DELTA_XS = [
        0.0000,
        0.1951,
        0.3827,
        0.5556,
        0.7071,
        0.8315,
        0.9239,
        0.9808,
        1.0000,
        0.9808,
        0.9239,
        0.8315,
        0.7071,
        0.5556,
        0.3827,
        0.1951,
        0.0000,
        -0.1951,
        -0.3827,
        -0.5556,
        -0.7071,
        -0.8315,
        -0.9239,
        -0.9808,
        -1.0000,
        -0.9808,
        -0.9239,
        -0.8315,
        -0.7071,
        -0.5556,
        -0.3827,
        -0.1951,
    ]

    DELTA_YS = [
        1.0000,
        0.9808,
        0.9239,
        0.8315,
        0.7071,
        0.5556,
        0.3827,
        0.1951,
        0.0000,
        -0.1951,
        -0.3827,
        -0.5556,
        -0.7071,
        -0.8315,
        -0.9239,
        -0.9808,
        -1.0000,
        -0.9808,
        -0.9239,
        -0.8315,
        -0.7071,
        -0.5556,
        -0.3827,
        -0.1951,
        -0.0000,
        0.1951,
        0.3827,
        0.5556,
        0.7071,
        0.8315,
        0.9239,
        0.9808,
    ]

    def move(self):
        self.y += Ship.DELTA_YS[self.heading] * self.speed
        self.x += Ship.DELTA_XS[self.heading] * self.speed

    def is_island_visible(self, island):
        delta_x = island.x - self.x
        delta_y = island.y - self.y
        return math.sqrt(delta_x * delta_x + delta_y * delta_y) <= 10

    def filter_visible_islands(self, islands):
        return [island for island in islands if self.is_island_visible(island)]

    def can_dock(self, island):
        delta_x = island.x - self.x
        delta_y = island.y - self.y
        return math.sqrt(delta_x * delta_x + delta_y * delta_y) < 2

    def filter_dockworthy_islands(self, islands):
        pass


class Island:
    def __init__(self, x, y):
        self.x = x
        self.y = y
