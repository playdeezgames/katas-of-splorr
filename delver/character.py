import direction


class Character:
    def __init__(self, new_dungeon, character_x=0, character_y=0):
        self.facing = direction.NORTH
        self.x = character_x
        self.y = character_y
        self.dungeon = new_dungeon
        self.__place_in_room()

    def set_facing(self, new_facing) -> None:
        if new_facing in direction.VALID_DIRECTIONS:
            self.facing = new_facing

    def turn_left(self) -> None:
        self.facing = direction.LEFTS[self.facing]

    def turn_right(self) -> None:
        self.facing = direction.RIGHTS[self.facing]

    def turn_around(self):
        self.facing = direction.OPPOSITES[self.facing]

    def __move_in_direction(self, move_direction) -> None:
        room = self.dungeon.get_room(self.x, self.y)
        if not room.has_exit(move_direction):
            return
        delta = direction.DELTAS[move_direction]
        self.move_to(self.x + delta[0], self.y + delta[1])

    def move_ahead(self) -> None:
        self.__move_in_direction(self.facing)

    def move_left(self) -> None:
        self.__move_in_direction(direction.LEFTS[self.facing])

    def move_right(self) -> None:
        self.__move_in_direction(direction.RIGHTS[self.facing])

    def move_back(self) -> None:
        self.__move_in_direction(direction.OPPOSITES[self.facing])

    def move_to(self, x, y) -> None:
        if (0 <= x < self.dungeon.columns) and (0 <= y < self.dungeon.rows):
            self.__remove_from_room()
            self.x = x
            self.y = y
            self.__place_in_room()

    def __get_room(self):
        return self.dungeon.get_room(self.x, self.y)

    def __remove_from_room(self):
        my_room = self.__get_room()
        my_room.characters = [c for c in my_room.characters if c != self]

    def __place_in_room(self):
        self.__get_room().place_character(self)
