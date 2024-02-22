NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

VALID_DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


class Character:
    def __init__(self):
        self.facing = NORTH

    def set_facing(self, new_facing):
        if new_facing in VALID_DIRECTIONS:
            self.facing = new_facing
