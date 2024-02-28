import pytest
import character
import direction
import room


def __create_character_sut(my_room):
    return character.Character(None, 0, 0, my_room)


def test_character_exists_and_initially_faces_north():
    sut = __create_character_sut(room.Room())
    assert sut.facing == direction.NORTH


@pytest.mark.parametrize(
    "given_facing, expected_facing",
    [
        (direction.EAST, direction.EAST),
        (direction.SOUTH, direction.SOUTH),
        (direction.WEST, direction.WEST),
        (99, direction.NORTH),
    ])
def test_character_set_facing(given_facing, expected_facing):
    sut = __create_character_sut(room.Room())
    sut.set_facing(given_facing)
    assert sut.facing == expected_facing


@pytest.mark.parametrize("given_initial_facing, expected_final_facing", [
    (direction.NORTH, direction.WEST),
    (direction.WEST, direction.SOUTH),
    (direction.SOUTH, direction.EAST),
    (direction.EAST, direction.NORTH),
])
def test_character_turn_left(given_initial_facing, expected_final_facing):
    sut = __create_character_sut(room.Room())
    sut.set_facing(given_initial_facing)
    sut.turn_left()
    assert sut.facing == expected_final_facing


@pytest.mark.parametrize("given_initial_facing, expected_final_facing", [
    (direction.NORTH, direction.EAST),
    (direction.EAST, direction.SOUTH),
    (direction.SOUTH, direction.WEST),
    (direction.WEST, direction.NORTH),
])
def test_character_turn_right(given_initial_facing, expected_final_facing):
    sut = __create_character_sut(room.Room())
    sut.set_facing(given_initial_facing)
    sut.turn_right()
    assert sut.facing == expected_final_facing


@pytest.mark.parametrize("given_initial_facing, expected_final_facing", [
    (direction.NORTH, direction.SOUTH),
    (direction.EAST, direction.WEST),
    (direction.SOUTH, direction.NORTH),
    (direction.WEST, direction.EAST),
])
def test_character_turn_around(given_initial_facing, expected_final_facing):
    sut = __create_character_sut(room.Room())
    sut.set_facing(given_initial_facing)
    sut.turn_around()
    assert sut.facing == expected_final_facing


def test_character_is_blocked_when_exit_does_not_exist_for_room():
    my_room = room.Room()
    sut = __create_character_sut(my_room)
    sut.move_ahead()
    assert sut.get_room() == my_room


@pytest.mark.parametrize("given_direction", [direction.NORTH, direction.EAST, direction.SOUTH, direction.WEST])
def test_character_allows_move_to_room_ahead(given_direction):
    next_room = room.Room()
    my_room = room.Room()
    my_room.set_neighbor(given_direction, next_room)
    my_room.set_exit(given_direction, True)
    sut = __create_character_sut(my_room)
    sut.set_facing(given_direction)
    sut.move_ahead()
    assert sut.get_room() == next_room


@pytest.mark.parametrize("given_direction", [direction.NORTH, direction.EAST, direction.SOUTH, direction.WEST])
def test_character_allows_move_to_room_left(given_direction):
    next_room = room.Room()
    my_room = room.Room()
    left_direction = direction.LEFTS[given_direction]
    my_room.set_neighbor(left_direction, next_room)
    my_room.set_exit(left_direction, True)
    sut = __create_character_sut(my_room)
    sut.set_facing(given_direction)
    sut.move_left()
    assert sut.get_room() == next_room


@pytest.mark.parametrize("given_direction", [direction.NORTH, direction.EAST, direction.SOUTH, direction.WEST])
def test_character_allows_move_to_room_right(given_direction):
    next_room = room.Room()
    my_room = room.Room()
    right_direction = direction.RIGHTS[given_direction]
    my_room.set_neighbor(right_direction, next_room)
    my_room.set_exit(right_direction, True)
    sut = __create_character_sut(my_room)
    sut.set_facing(given_direction)
    sut.move_right()
    assert sut.get_room() == next_room


@pytest.mark.parametrize("given_direction", [direction.NORTH, direction.EAST, direction.SOUTH, direction.WEST])
def test_character_allows_move_to_room_behind(given_direction):
    next_room = room.Room()
    my_room = room.Room()
    back_direction = direction.OPPOSITES[given_direction]
    my_room.set_neighbor(back_direction, next_room)
    my_room.set_exit(back_direction, True)
    sut = __create_character_sut(my_room)
    sut.set_facing(given_direction)
    sut.move_back()
    assert sut.get_room() == next_room
