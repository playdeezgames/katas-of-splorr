import pytest
import dungeon
import character
import direction
import room


def test_character_exists_and_initially_faces_north():
    sut = character.Character(dungeon.Dungeon(1, 1))
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
    sut = character.Character(dungeon.Dungeon(1, 1))
    sut.set_facing(given_facing)
    assert sut.facing == expected_facing


@pytest.mark.parametrize("given_initial_facing, expected_final_facing", [
    (direction.NORTH, direction.WEST),
    (direction.WEST, direction.SOUTH),
    (direction.SOUTH, direction.EAST),
    (direction.EAST, direction.NORTH),
])
def test_character_turn_left(given_initial_facing, expected_final_facing):
    sut = character.Character(dungeon.Dungeon(1, 1))
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
    sut = character.Character(dungeon.Dungeon(1, 1))
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
    sut = character.Character(dungeon.Dungeon(1, 1))
    sut.set_facing(given_initial_facing)
    sut.turn_around()
    assert sut.facing == expected_final_facing


def test_characters_have_x_and_y():
    sut = character.Character(dungeon.Dungeon(1, 1))
    assert sut.x == 0
    assert sut.y == 0


def __prep_dungeon_for_move_test(offset_x, offset_y, given_facing):
    dungeon_columns = offset_x * 2 + 1
    dungeon_rows = offset_y * 2 + 1
    my_dungeon = dungeon.Dungeon(dungeon_columns, dungeon_rows)
    for column in range(dungeon_columns):
        for row in range(dungeon_rows):
            room = my_dungeon.get_room(column, row)
            room.set_exit(given_facing, True)
    return my_dungeon


@pytest.mark.parametrize("given_facing, steps, expected_delta_x, expected_delta_y", [
    (direction.NORTH, 1, 0, 1),
    (direction.SOUTH, 1, 0, -1),
    (direction.EAST, 1, 1, 0),
    (direction.WEST, 1, -1, 0),
    (direction.NORTH, 2, 0, 2),
    (direction.SOUTH, 2, 0, -2),
    (direction.EAST, 2, 2, 0),
    (direction.WEST, 2, -2, 0),
])
def test_character_moves_ahead(given_facing, steps, expected_delta_x, expected_delta_y):
    offset_x = 2
    offset_y = 2
    my_dungeon = __prep_dungeon_for_move_test(offset_x, offset_y, given_facing)
    sut = character.Character(my_dungeon)
    sut.move_to_xy(offset_x, offset_y)
    sut.set_facing(given_facing)
    for step in range(steps):
        sut.move_ahead()
    assert sut.facing == given_facing
    assert sut.x == expected_delta_x + offset_x
    assert sut.y == expected_delta_y + offset_y


@pytest.mark.parametrize("given_facing, steps, expected_delta_x, expected_delta_y", [
    (direction.NORTH, 1, -1, 0),
    (direction.NORTH, 2, -2, 0),
    (direction.SOUTH, 1, 1, 0),
    (direction.SOUTH, 2, 2, 0),
    (direction.EAST, 1, 0, 1),
    (direction.EAST, 2, 0, 2),
    (direction.WEST, 1, 0, -1),
    (direction.WEST, 2, 0, -2),
])
def test_character_moves_left(given_facing, steps, expected_delta_x, expected_delta_y):
    offset_x = 2
    offset_y = 2
    my_dungeon = __prep_dungeon_for_move_test(offset_x, offset_y, direction.LEFTS[given_facing])
    sut = character.Character(my_dungeon)
    sut.move_to_xy(offset_x, offset_y)
    sut.set_facing(given_facing)
    for step in range(steps):
        sut.move_left()
    assert sut.facing == given_facing
    assert sut.x == expected_delta_x + offset_x
    assert sut.y == expected_delta_y + offset_y


@pytest.mark.parametrize("given_facing, steps, expected_delta_x, expected_delta_y", [
    (direction.NORTH, 1, 1, 0),
    (direction.NORTH, 2, 2, 0),
    (direction.SOUTH, 1, -1, 0),
    (direction.SOUTH, 2, -2, 0),
    (direction.EAST, 1, 0, -1),
    (direction.EAST, 2, 0, -2),
    (direction.WEST, 1, 0, 1),
    (direction.WEST, 2, 0, 2),
])
def test_character_moves_right(given_facing, steps, expected_delta_x, expected_delta_y):
    offset_x = 2
    offset_y = 2
    my_dungeon = __prep_dungeon_for_move_test(offset_x, offset_y, direction.RIGHTS[given_facing])
    sut = character.Character(my_dungeon)
    sut.move_to_xy(offset_x, offset_y)
    sut.set_facing(given_facing)
    for step in range(steps):
        sut.move_right()
    assert sut.facing == given_facing
    assert sut.x == expected_delta_x + offset_x
    assert sut.y == expected_delta_y + offset_y


@pytest.mark.parametrize("given_facing, steps, expected_delta_x, expected_delta_y", [
    (direction.NORTH, 1, 0, -1),
    (direction.SOUTH, 1, 0, 1),
    (direction.EAST, 1, -1, 0),
    (direction.WEST, 1, 1, 0),
    (direction.NORTH, 2, 0, -2),
    (direction.SOUTH, 2, 0, 2),
    (direction.EAST, 2, -2, 0),
    (direction.WEST, 2, 2, 0),
])
def test_character_moves_back(given_facing, steps, expected_delta_x, expected_delta_y):
    offset_x = 2
    offset_y = 2
    my_dungeon = __prep_dungeon_for_move_test(offset_x, offset_y, direction.OPPOSITES[given_facing])
    sut = character.Character(my_dungeon)
    sut.move_to_xy(offset_x, offset_y)
    sut.set_facing(given_facing)
    for step in range(steps):
        sut.move_back()
    assert sut.facing == given_facing
    assert sut.x == expected_delta_x + offset_x
    assert sut.y == expected_delta_y + offset_y


def test_characters_must_be_in_dungeon():
    given_dungeon = dungeon.Dungeon(1, 1)
    sut = character.Character(given_dungeon)
    assert sut.dungeon == given_dungeon, "Character must be in a dungeon"


@pytest.mark.parametrize("dungeon_columns, dungeon_rows, given_x, given_y, expected_x, expected_y", [
    (2, 2, 0, 1, 0, 1),
    (2, 2, 1, 1, 1, 1),
    (2, 2, 2, 1, 0, 0),
])
def test_character_can_move_within_dungeon(dungeon_columns, dungeon_rows, given_x, given_y, expected_x, expected_y):
    given_dungeon = dungeon.Dungeon(dungeon_columns, dungeon_rows)
    sut = character.Character(given_dungeon)
    sut.move_to_xy(given_x, given_y)
    assert sut.x == expected_x
    assert sut.y == expected_y


def test_character_is_blocked_when_exit_does_not_exist_for_room():
    given_dungeon = dungeon.Dungeon(3, 3)
    sut = character.Character(given_dungeon)
    sut.move_to_xy(1, 1)
    sut.move_ahead()
    assert sut.x == 1
    assert sut.y == 1


def test_character_lacks_room_tracking_toggle():
    sut = character.Character(dungeon.Dungeon(1, 1))
    assert not sut.track_room


def test_character_tracks_room():
    my_room = room.Room()
    sut = character.Character(None, 0, 0, my_room)
    assert sut.track_room


@pytest.mark.parametrize("given_direction", [direction.NORTH, direction.EAST, direction.SOUTH, direction.WEST])
def test_character_allows_move_to_room_ahead(given_direction):
    next_room = room.Room()
    my_room = room.Room()
    my_room.set_neighbor(given_direction, next_room)
    my_room.set_exit(given_direction, True)
    sut = character.Character(None, 0, 0, my_room)
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
    sut = character.Character(None, 0, 0, my_room)
    sut.set_facing(given_direction)
    sut.move_left()
    assert sut.get_room() == next_room
