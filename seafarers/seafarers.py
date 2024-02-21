class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 0

    def set_heading(self, new_heading):
        self.heading = new_heading % 32
