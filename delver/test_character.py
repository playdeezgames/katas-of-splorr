import pytest

import character


def test_character_exists_and_initially_faces_north():
    sut = character.Character()
    assert sut.facing == character.NORTH


@pytest.mark.parametrize(
    "given_facing, expected_facing",
    [
        (character.EAST, character.EAST),
        (character.SOUTH, character.SOUTH),
        (character.WEST, character.WEST),
        (99, character.NORTH),
    ])
def test_character_set_facing(given_facing, expected_facing):
    sut = character.Character()
    sut.set_facing(given_facing)
    assert sut.facing == expected_facing


@pytest.mark.parametrize("given_initial_facing, expected_final_facing", [
    (character.NORTH, character.WEST),
    (character.WEST, character.SOUTH),
    (character.SOUTH, character.EAST),
    (character.EAST, character.NORTH),
])
def test_character_turn_left(given_initial_facing, expected_final_facing):
    sut = character.Character()
    sut.set_facing(given_initial_facing)
    sut.turn_left()
    assert sut.facing == expected_final_facing


@pytest.mark.parametrize("given_initial_facing, expected_final_facing", [
    (character.NORTH, character.EAST),
    (character.EAST, character.SOUTH),
    (character.SOUTH, character.WEST),
    (character.WEST, character.NORTH),
])
def test_character_turn_right(given_initial_facing, expected_final_facing):
    sut = character.Character()
    sut.set_facing(given_initial_facing)
    sut.turn_right()
    assert sut.facing == expected_final_facing


@pytest.mark.parametrize("given_initial_facing, expected_final_facing", [
    (character.NORTH, character.SOUTH),
    (character.EAST, character.WEST),
    (character.SOUTH, character.NORTH),
    (character.WEST, character.EAST),
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
    (character.NORTH, 1, 0, 1),
    (character.SOUTH, 1, 0, -1),
    (character.EAST, 1, 1, 0),
    (character.WEST, 1, -1, 0),
    (character.NORTH, 2, 0, 2),
    (character.SOUTH, 2, 0, -2),
    (character.EAST, 2, 2, 0),
    (character.WEST, 2, -2, 0),
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
    (character.NORTH, 1, -1, 0),
    (character.NORTH, 2, -2, 0),
    (character.SOUTH, 1, 1, 0),
    (character.SOUTH, 2, 2, 0),
    (character.EAST, 1, 0, 1),
    (character.EAST, 2, 0, 2),
    (character.WEST, 1, 0, -1),
    (character.WEST, 2, 0, -2),
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
    (character.NORTH, 1, 1, 0),
    (character.NORTH, 2, 2, 0),
    (character.SOUTH, 1, -1, 0),
    (character.SOUTH, 2, -2, 0),
    (character.EAST, 1, 0, -1),
    (character.EAST, 2, 0, -2),
    (character.WEST, 1, 0, 1),
    (character.WEST, 2, 0, 2),
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
    (character.NORTH, 1, 0, -1),
    (character.SOUTH, 1, 0, 1),
    (character.EAST, 1, -1, 0),
    (character.WEST, 1, 1, 0),
    (character.NORTH, 2, 0, -2),
    (character.SOUTH, 2, 0, 2),
    (character.EAST, 2, -2, 0),
    (character.WEST, 2, 2, 0),
])
def test_character_moves_back(given_facing, steps, expected_x, expected_y):
    sut = character.Character()
    sut.set_facing(given_facing)
    for step in range(steps):
        sut.move_back()
    assert sut.facing == given_facing
    assert sut.x == expected_x
    assert sut.y == expected_y
