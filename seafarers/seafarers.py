import math


class Island:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ship:
    def set_heading(self, new_heading):
        self.heading = new_heading - (new_heading // 360) * 360

    def set_speed(self, new_speed):
        self.speed = min(max(new_speed, 0), 1)

    def move(self):
        self.y += math.cos(self.heading * math.pi / 180) * self.speed
        self.x += math.sin(self.heading * math.pi / 180) * self.speed

    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 0
        self.speed = 1
