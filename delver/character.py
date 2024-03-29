import direction
import feature
import inventory


class Character:
    def __init__(self, new_room):
        self.facing = direction.NORTH
        self.room = new_room
        self.health = 3
        self.inventory = inventory.Inventory()
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

    def get_inventory(self):
        return self.inventory

    def pick_up_item(self, item):
        if self.get_room().get_inventory().contains_item(item):
            self.get_room().get_inventory().remove_item(item)
            self.get_inventory().add_item(item)

    def drop_item(self, item):
        if self.get_inventory().contains_item(item):
            self.get_inventory().remove_item(item)
            self.get_room().get_inventory().add_item(item)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            my_corpse = feature.Feature()
            self.get_room().add_feature(my_corpse)
            for item in self.get_inventory().items:
                self.get_inventory().remove_item(item)
                my_corpse.get_inventory().add_item(item)
            self.__remove_from_room()
