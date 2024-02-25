import direction


class Character:
    def __init__(self, new_dungeon):
        self.facing = direction.NORTH
        self.x = 0
        self.y = 0
        self.dungeon = new_dungeon
        self.check_room_exits = False

    def set_facing(self, new_facing):
        if new_facing in direction.VALID_DIRECTIONS:
            self.facing = new_facing

    def turn_left(self):
        self.facing = [direction.WEST, direction.NORTH, direction.EAST, direction.SOUTH][self.facing]

    def turn_right(self):
        self.facing = [direction.EAST, direction.SOUTH, direction.WEST, direction.NORTH][self.facing]

    def turn_around(self):
        self.facing = [direction.SOUTH, direction.WEST, direction.NORTH, direction.EAST][self.facing]

    def move_ahead(self):
        if self.facing == direction.SOUTH:
            self.y += -1
        elif self.facing == direction.EAST:
            self.x += 1
        elif self.facing == direction.WEST:
            self.x += -1
        else:
            self.y += 1

    def move_left(self):
        self.turn_left()
        self.move_ahead()
        self.turn_right()

    def move_right(self):
        self.turn_right()
        self.move_ahead()
        self.turn_left()

    def move_back(self):
        self.turn_around()
        self.move_ahead()
        self.turn_around()

    def move_to(self, x, y):
        if (0 <= x < self.dungeon.columns) and (0 <= y < self.dungeon.rows):
            self.x = x
            self.y = y
