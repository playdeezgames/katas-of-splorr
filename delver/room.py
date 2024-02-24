import direction


class Room:
    def __init__(self):
        self.exits = [False for _ in range(len(direction.VALID_DIRECTIONS))]

    def has_exit(self, exit_direction):
        return self.exits[exit_direction]

    def set_exit(self, exit_direction, exit_state):
        self.exits[exit_direction] = exit_state
