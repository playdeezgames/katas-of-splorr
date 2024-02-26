import pytest

import character
import dungeon
import room
import direction


def test_room_exists():
    sut = room.Room()
    assert not sut.has_exit(direction.NORTH), "room has exit to the north, but should not"
    assert not sut.has_exit(direction.EAST), "room has exit to the east, but should not"
    assert not sut.has_exit(direction.SOUTH), "room has exit to the south, but should not"
    assert not sut.has_exit(direction.WEST), "room has exit to the west, but should not"


@pytest.mark.parametrize("given_direction", [
    direction.NORTH,
])
def test_room_set_exit(given_direction):
    sut = room.Room()
    sut.set_exit(given_direction, True)
    assert sut.has_exit(given_direction), f"room does not have an exit in direction {given_direction}"


@pytest.mark.parametrize("dungeon_columns, dungeon_rows, room_column, room_row, expected_result", [
    (1, 1, 0, 0, True),
    (2, 1, 1, 0, False),
])
def test_room_contains_character(dungeon_columns, dungeon_rows, room_column, room_row, expected_result):
    my_dungeon = dungeon.Dungeon(dungeon_columns, dungeon_rows)
    sut = my_dungeon.get_room(room_column, room_row)
    my_character = character.Character(my_dungeon)
    assert sut.contains_character(my_character) == expected_result
