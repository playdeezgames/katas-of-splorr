class Ship:
    def set_heading(self, new_heading):
        self.heading = new_heading - (new_heading // 360) * 360

    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 0
        self.speed = 1
