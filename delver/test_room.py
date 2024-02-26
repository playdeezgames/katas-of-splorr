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
def test_room_contains_character_when_created(dungeon_columns, dungeon_rows, room_column, room_row, expected_result):
    my_dungeon = dungeon.Dungeon(dungeon_columns, dungeon_rows)
    sut = my_dungeon.get_room(room_column, room_row)
    my_character = character.Character(my_dungeon)
    assert sut.contains_character(my_character) == expected_result


@pytest.mark.parametrize(
    "dungeon_columns, dungeon_rows, initial_room_column, initial_room_row, final_room_column, final_room_row",
    [
        (2, 1, 0, 0, 1, 0),
    ])
def test_room_contains_character_when_teleported(
        dungeon_columns,
        dungeon_rows,
        initial_room_column,
        initial_room_row,
        final_room_column,
        final_room_row):
    my_dungeon = dungeon.Dungeon(dungeon_columns, dungeon_rows)
    my_character = character.Character(my_dungeon, initial_room_column, initial_room_row)
    initial_room = my_dungeon.get_room(initial_room_column, initial_room_row)
    final_room = my_dungeon.get_room(final_room_column, final_room_row)
    my_character.move_to(final_room_column, final_room_row)
    assert not initial_room.contains_character(my_character)
    assert final_room.contains_character(my_character)


@pytest.mark.parametrize(
    "given_direction",
    [
        direction.NORTH,
    ])
def test_room_contains_character_when_moved_ahead(given_direction):
    my_dungeon = dungeon.Dungeon(3, 3)
    my_character = character.Character(my_dungeon, 1, 1)
    initial_room = my_dungeon.get_room(my_character.x, my_character.y)
    initial_room.set_exit(given_direction, True)
    my_character.set_facing(given_direction)
    my_character.move_ahead()
    final_room = my_dungeon.get_room(my_character.x, my_character.y)
    assert not initial_room.contains_character(my_character)
    assert final_room.contains_character(my_character)


@pytest.mark.parametrize(
    "given_direction",
    [
        direction.NORTH,
    ])
def test_room_contains_character_when_moved_left(given_direction):
    my_dungeon = dungeon.Dungeon(3, 3)
    my_character = character.Character(my_dungeon, 1, 1)
    initial_room = my_dungeon.get_room(my_character.x, my_character.y)
    initial_room.set_exit(direction.LEFTS[given_direction], True)
    my_character.set_facing(given_direction)
    my_character.move_left()
    final_room = my_dungeon.get_room(my_character.x, my_character.y)
    assert not initial_room.contains_character(my_character)
    assert final_room.contains_character(my_character)


@pytest.mark.parametrize(
    "given_direction",
    [
        direction.NORTH,
    ])
def test_room_contains_character_when_moved_right(given_direction):
    my_dungeon = dungeon.Dungeon(3, 3)
    my_character = character.Character(my_dungeon, 1, 1)
    initial_room = my_dungeon.get_room(my_character.x, my_character.y)
    initial_room.set_exit(direction.RIGHTS[given_direction], True)
    my_character.set_facing(given_direction)
    my_character.move_right()
    final_room = my_dungeon.get_room(my_character.x, my_character.y)
    assert not initial_room.contains_character(my_character)
    assert final_room.contains_character(my_character)


@pytest.mark.parametrize(
    "given_direction",
    [
        direction.NORTH,
    ])
def test_room_contains_character_when_moved_back(given_direction):
    my_dungeon = dungeon.Dungeon(3, 3)
    my_character = character.Character(my_dungeon, 1, 1)
    initial_room = my_dungeon.get_room(my_character.x, my_character.y)
    initial_room.set_exit(direction.OPPOSITES[given_direction], True)
    my_character.set_facing(given_direction)
    my_character.move_back()
    final_room = my_dungeon.get_room(my_character.x, my_character.y)
    assert not initial_room.contains_character(my_character)
    assert final_room.contains_character(my_character)


def test_room_add_character():
    sut = room.Room()
    my_character = character.Character(dungeon.Dungeon(1, 1))
    sut.place_character(my_character)
    assert sut.contains_character(my_character)


def test_room_remove_character():
    sut = room.Room()
    my_character = character.Character(dungeon.Dungeon(1, 1))
    sut.place_character(my_character)
    sut.remove_character(my_character)
    assert not sut.contains_character(my_character)
