import room


class Dungeon:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.rooms = [room.Room() for _ in range(columns * rows)]

    def get_room(self, column, row):
        return self.rooms[column + row * self.columns]