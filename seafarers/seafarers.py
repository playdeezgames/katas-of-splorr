class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 0
        self.speed = 1

    def set_heading(self, new_heading):
        self.heading = new_heading % 32

    def set_speed(self, new_speed):
        self.speed = max(0, min(1, new_speed))
