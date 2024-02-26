import character
import direction


class Room:
    def __init__(self):
        self.exits = [False for _ in range(len(direction.VALID_DIRECTIONS))]
        self.characters = []

    def has_exit(self, exit_direction) -> bool:
        return self.exits[exit_direction]

    def set_exit(self, exit_direction, exit_state) -> None:
        self.exits[exit_direction] = exit_state

    def contains_character(self, candidate_character: character.Character) -> bool:
        return candidate_character in self.characters

