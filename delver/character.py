import direction


class Character:
    def __init__(self, new_dungeon=None, character_x=0, character_y=0, new_room=None):
        self.facing = direction.NORTH
        self.room = new_room
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
        room = self.get_room()
        if not room.has_exit(move_direction):
            return
        self.__remove_from_room()
        self.room = room.get_neighbor(move_direction)
        self.__place_in_room()

    def move_ahead(self) -> None:
        self.__move_in_direction(self.facing)

    def move_left(self) -> None:
        self.__move_in_direction(direction.LEFTS[self.facing])

    def move_right(self) -> None:
        self.__move_in_direction(direction.RIGHTS[self.facing])

    def move_back(self) -> None:
        self.__move_in_direction(direction.OPPOSITES[self.facing])

    def get_room(self):
        return self.room

    def __remove_from_room(self):
        self.get_room().remove_character(self)

    def __place_in_room(self):
        self.get_room().place_character(self)
