import pytest

import delver


def test_character_exists_and_initially_faces_north():
    sut = delver.Character()
    assert sut.facing == delver.NORTH


@pytest.mark.parametrize(
    "given_facing, expected_facing",
    [
        (delver.EAST, delver.EAST),
        (delver.SOUTH, delver.SOUTH),
        (delver.WEST, delver.WEST),
        (99, delver.NORTH),
    ])
def test_character_set_facing(given_facing, expected_facing):
    sut = delver.Character()
    sut.set_facing(given_facing)
    assert sut.facing == expected_facing


@pytest.mark.parametrize("given_initial_facing, expected_final_facing", [
    (delver.NORTH, delver.WEST),
    (delver.WEST, delver.SOUTH),
    (delver.SOUTH, delver.EAST),
    (delver.EAST, delver.NORTH),
])
def test_character_turn_left(given_initial_facing, expected_final_facing):
    sut = delver.Character()
    sut.set_facing(given_initial_facing)
    sut.turn_left()
    assert sut.facing == expected_final_facing


@pytest.mark.parametrize("given_initial_facing, expected_final_facing", [
    (delver.NORTH, delver.EAST),
    (delver.EAST, delver.SOUTH),
    (delver.SOUTH, delver.WEST),
    (delver.WEST, delver.NORTH),
])
def test_character_turn_right(given_initial_facing, expected_final_facing):
    sut = delver.Character()
    sut.set_facing(given_initial_facing)
    sut.turn_right()
    assert sut.facing == expected_final_facing


@pytest.mark.parametrize("given_initial_facing, expected_final_facing", [
    (delver.NORTH, delver.SOUTH),
    (delver.EAST, delver.WEST),
    (delver.SOUTH, delver.NORTH),
    (delver.WEST, delver.EAST),
])
def test_character_turn_around(given_initial_facing, expected_final_facing):
    sut = delver.Character()
    sut.set_facing(given_initial_facing)
    sut.turn_around()
    assert sut.facing == expected_final_facing


def test_characters_have_x_and_y():
    sut = delver.Character()
    assert sut.x == 0
    assert sut.y == 0


@pytest.mark.parametrize("given_facing, steps, expected_x, expected_y", [
    (delver.NORTH, 1, 0, 1),
    (delver.SOUTH, 1, 0, -1),
    (delver.EAST, 1, 1, 0),
    (delver.WEST, 1, -1, 0),
    (delver.NORTH, 2, 0, 2),
    (delver.SOUTH, 2, 0, -2),
    (delver.EAST, 2, 2, 0),
    (delver.WEST, 2, -2, 0),
])
def test_character_moves_ahead(given_facing, steps, expected_x, expected_y):
    sut = delver.Character()
    sut.set_facing(given_facing)
    for step in range(steps):
        sut.move_ahead()
    assert sut.x == expected_x
    assert sut.y == expected_y


@pytest.mark.parametrize("given_facing, steps, expected_x, expected_y", [
    (delver.NORTH, 1, -1, 0),
    (delver.NORTH, 2, -2, 0),
    (delver.SOUTH, 1, 1, 0),
    (delver.SOUTH, 2, 2, 0),
    (delver.EAST, 1, 0, 1),
    (delver.EAST, 2, 0, 2),
    (delver.WEST, 1, 0, -1),
    (delver.WEST, 2, 0, -2),
])
def test_character_moves_left(given_facing, steps, expected_x, expected_y):
    sut = delver.Character()
    sut.set_facing(given_facing)
    for step in range(steps):
        sut.move_left()
    assert sut.x == expected_x
    assert sut.y == expected_y


@pytest.mark.parametrize("given_facing, steps, expected_x, expected_y", [
    (delver.NORTH, 1, 1, 0),
    (delver.NORTH, 2, 2, 0),
    (delver.SOUTH, 1, -1, 0),
    (delver.SOUTH, 2, -2, 0),
    (delver.EAST, 1, 0, -1),
    (delver.EAST, 2, 0, -2),
    (delver.WEST, 1, 0, 1),
    (delver.WEST, 2, 0, 2),
])
def test_character_moves_right(given_facing, steps, expected_x, expected_y):
    sut = delver.Character()
    sut.set_facing(given_facing)
    for step in range(steps):
        sut.move_right()
    assert sut.x == expected_x
    assert sut.y == expected_y
