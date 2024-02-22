import math


def filter_islands(islands, is_island_visible):
    return [island for island in islands if is_island_visible(island)]


class Ship:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 0
        self.speed = 1
        self.docked_at = None
        self.moves = 0

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
        if self.docked_at is None:
            self.moves += 1
            self.y += Ship.DELTA_YS[self.heading] * self.speed
            self.x += Ship.DELTA_XS[self.heading] * self.speed

    def distance_to(self, island):
        delta_x = island.x - self.x
        delta_y = island.y - self.y
        return math.sqrt(delta_x * delta_x + delta_y * delta_y)

    def is_island_visible(self, island):
        return self.distance_to(island) <= 10

    def filter_visible_islands(self, islands):
        return filter_islands(islands, self.is_island_visible)

    def can_dock(self, island):
        return self.distance_to(island) < 2

    def filter_dockworthy_islands(self, islands):
        return filter_islands(islands, self.can_dock)

    def dock(self, island):
        self.moves += 1
        self.docked_at = island

    def rough_heading_to(self, island):
        if island.x > self.x:
            if island.y > self.y:
                return 4
            elif island.y < self.y:
                return 12
            return 8
        elif island.x < self.x:
            if island.y > self.y:
                return 28
            elif island.y < self.y:
                return 20
            return 24
        if island.y >= self.y:
            return 0
        return 16



class Island:
    def __init__(self, x, y):
        self.x = x
        self.y = y
