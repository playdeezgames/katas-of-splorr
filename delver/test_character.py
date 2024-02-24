import pytest

import character
import direction


def test_character_exists_and_initially_faces_north():
    sut = character.Character()
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
    sut = character.Character()
    sut.set_facing(given_facing)
    assert sut.facing == expected_facing


@pytest.mark.parametrize("given_initial_facing, expected_final_facing", [
    (direction.NORTH, direction.WEST),
    (direction.WEST, direction.SOUTH),
    (direction.SOUTH, direction.EAST),
    (direction.EAST, direction.NORTH),
])
def test_character_turn_left(given_initial_facing, expected_final_facing):
    sut = character.Character()
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
    sut = character.Character()
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
    sut = character.Character()
    sut.set_facing(given_initial_facing)
    sut.turn_around()
    assert sut.facing == expected_final_facing


def test_characters_have_x_and_y():
    sut = character.Character()
    assert sut.x == 0
    assert sut.y == 0


@pytest.mark.parametrize("given_facing, steps, expected_x, expected_y", [
    (direction.NORTH, 1, 0, 1),
    (direction.SOUTH, 1, 0, -1),
    (direction.EAST, 1, 1, 0),
    (direction.WEST, 1, -1, 0),
    (direction.NORTH, 2, 0, 2),
    (direction.SOUTH, 2, 0, -2),
    (direction.EAST, 2, 2, 0),
    (direction.WEST, 2, -2, 0),
])
def test_character_moves_ahead(given_facing, steps, expected_x, expected_y):
    sut = character.Character()
    sut.set_facing(given_facing)
    for step in range(steps):
        sut.move_ahead()
    assert sut.facing == given_facing
    assert sut.x == expected_x
    assert sut.y == expected_y


@pytest.mark.parametrize("given_facing, steps, expected_x, expected_y", [
    (direction.NORTH, 1, -1, 0),
    (direction.NORTH, 2, -2, 0),
    (direction.SOUTH, 1, 1, 0),
    (direction.SOUTH, 2, 2, 0),
    (direction.EAST, 1, 0, 1),
    (direction.EAST, 2, 0, 2),
    (direction.WEST, 1, 0, -1),
    (direction.WEST, 2, 0, -2),
])
def test_character_moves_left(given_facing, steps, expected_x, expected_y):
    sut = character.Character()
    sut.set_facing(given_facing)
    for step in range(steps):
        sut.move_left()
    assert sut.facing == given_facing
    assert sut.x == expected_x
    assert sut.y == expected_y


@pytest.mark.parametrize("given_facing, steps, expected_x, expected_y", [
    (direction.NORTH, 1, 1, 0),
    (direction.NORTH, 2, 2, 0),
    (direction.SOUTH, 1, -1, 0),
    (direction.SOUTH, 2, -2, 0),
    (direction.EAST, 1, 0, -1),
    (direction.EAST, 2, 0, -2),
    (direction.WEST, 1, 0, 1),
    (direction.WEST, 2, 0, 2),
])
def test_character_moves_right(given_facing, steps, expected_x, expected_y):
    sut = character.Character()
    sut.set_facing(given_facing)
    for step in range(steps):
        sut.move_right()
    assert sut.facing == given_facing
    assert sut.x == expected_x
    assert sut.y == expected_y


@pytest.mark.parametrize("given_facing, steps, expected_x, expected_y", [
    (direction.NORTH, 1, 0, -1),
    (direction.SOUTH, 1, 0, 1),
    (direction.EAST, 1, -1, 0),
    (direction.WEST, 1, 1, 0),
    (direction.NORTH, 2, 0, -2),
    (direction.SOUTH, 2, 0, 2),
    (direction.EAST, 2, -2, 0),
    (direction.WEST, 2, 2, 0),
])
def test_character_moves_back(given_facing, steps, expected_x, expected_y):
    sut = character.Character()
    sut.set_facing(given_facing)
    for step in range(steps):
        sut.move_back()
    assert sut.facing == given_facing
    assert sut.x == expected_x
    assert sut.y == expected_y
