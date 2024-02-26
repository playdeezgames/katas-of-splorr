import character
import direction


class Room:
    def __init__(self):
        self.exits = [False for _ in range(len(direction.VALID_DIRECTIONS))]
        self.neighbors = [None for _ in range(len(direction.VALID_DIRECTIONS))]
        self.characters = []

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
