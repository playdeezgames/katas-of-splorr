import direction
import inventory


class Room:
    def __init__(self):
        self.exits = [False for _ in range(len(direction.VALID_DIRECTIONS))]
        self.neighbors = [None for _ in range(len(direction.VALID_DIRECTIONS))]
        self.characters = []
        self.inventory = inventory.Inventory()
        self.features = []

    def has_exit(self, exit_direction) -> bool:
        return self.exits[exit_direction]

    def set_exit(self, exit_direction, exit_state) -> None:
        self.exits[exit_direction] = exit_state

    def contains_character(self, candidate_character) -> bool:
        return candidate_character in self.characters

    def place_character(self, new_character):
        self.characters.append(new_character)

    def remove_character(self, old_character):
        self.characters = [c for c in self.characters if c != old_character]

    def has_neighbor(self, which_direction):
        return self.neighbors[which_direction] is not None

    def set_neighbor(self, which_direction, new_neighbor):
        self.neighbors[which_direction] = new_neighbor

    def get_neighbor(self, which_direction):
        return self.neighbors[which_direction]

    def get_inventory(self):
        return self.inventory

    def has_feature(self, feature):
        return feature in self.features

    def add_feature(self, feature):
        if not self.has_feature(feature):
            feature.room = self
            self.features.append(feature)

    def remove_feature(self, feature):
        if self.has_feature(feature):
            self.features.remove(feature)
            feature.room = None
