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


def test_room_contains_character_when_created():
    sut = room.Room()
    my_character = character.Character(None, 0, 0, sut)
    assert sut.contains_character(my_character)


@pytest.mark.parametrize(
    "given_direction",
    [
        direction.NORTH,
        direction.EAST,
        direction.SOUTH,
        direction.WEST,
    ])
def test_room_contains_character_when_moved_ahead(given_direction):
    initial_room = room.Room()
    initial_room.set_exit(given_direction, True)
    final_room = room.Room()
    initial_room.set_neighbor(given_direction, final_room)
    my_character = character.Character(None, 1, 1, initial_room)
    my_character.set_facing(given_direction)
    my_character.move_ahead()
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


@pytest.mark.parametrize("given_direction", [
    direction.NORTH,
    direction.EAST,
    direction.SOUTH,
    direction.WEST,
])
def test_isolated_room_has_no_neighbors(given_direction):
    sut = room.Room()
    assert not sut.has_neighbor(given_direction)


def test_assign_neighbor_for_room():
    given_direction = direction.NORTH
    sut = room.Room()
    other_room = room.Room()
    sut.set_neighbor(given_direction, other_room)
    assert sut.has_neighbor(given_direction)
    actual = sut.get_neighbor(given_direction)
    assert actual == other_room
