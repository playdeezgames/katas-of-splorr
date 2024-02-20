import math


class Island:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ship:
    MAXIMUM_VISIBILITY = 10

    def set_heading(self, new_heading):
        self.heading = new_heading - (new_heading // 360) * 360

    def set_speed(self, new_speed):
        self.speed = min(max(new_speed, 0), 1)

    def move(self):
        self.y += math.cos(self.heading * math.pi / 180) * self.speed
        self.x += math.sin(self.heading * math.pi / 180) * self.speed

    def can_see(self, island):
        return math.sqrt(
            (self.x - island.x) * (self.x - island.x) +
            (self.y - island.y) * (self.y - island.y)) <= Ship.MAXIMUM_VISIBILITY

    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 0
        self.speed = 1
