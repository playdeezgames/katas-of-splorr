NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

VALID_DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


class Character:
    def __init__(self):
        self.facing = NORTH
        self.x = 0
        self.y = 0

    def set_facing(self, new_facing):
        if new_facing in VALID_DIRECTIONS:
            self.facing = new_facing

    def turn_left(self):
        self.facing = [WEST, NORTH, EAST, SOUTH][self.facing]

    def turn_right(self):
        self.facing = [EAST, SOUTH, WEST, NORTH][self.facing]

    def turn_around(self):
        self.facing = [SOUTH, WEST, NORTH, EAST][self.facing]

    def move_ahead(self):
        if self.facing == SOUTH:
            self.y += -1
        elif self.facing == EAST:
            self.x += 1
        elif self.facing == WEST:
            self.x += -1
        else:
            self.y += 1

    def move_left(self):
        self.turn_left()
        self.move_ahead()
        self.turn_right()

    def move_right(self):
        pass