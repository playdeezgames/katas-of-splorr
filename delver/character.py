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
        self.facing = direction.LEFTS[self.facing]

    def turn_right(self):
        self.facing = direction.RIGHTS[self.facing]

    def turn_around(self):
        self.facing = direction.OPPOSITES[self.facing]

    def move_ahead(self):
        if self.check_room_exits:
            room = self.dungeon.get_room(self.x, self.y)
            if not room.has_exit(self.facing):
                return
        delta = direction.DELTAS[self.facing]
        self.x += delta[0]
        self.y += delta[1]

    def move_left(self):
        self.turn_left()
        self.move_ahead()
        self.turn_right()

    def move_right(self):
        self.turn_right()
        self.move_ahead()
        self.turn_left()

    def move_back(self):
        old = self.check_room_exits
        self.check_room_exits = True
        self.turn_around()
        self.move_ahead()
        self.turn_around()
        self.check_room_exits = old

    def move_to(self, x, y):
        if (0 <= x < self.dungeon.columns) and (0 <= y < self.dungeon.rows):
            self.x = x
            self.y = y
