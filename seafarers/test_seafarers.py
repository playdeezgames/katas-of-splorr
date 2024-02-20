import math

import pytest

import seafarers


def test_ship_should_have_xy():
    actual = seafarers.Ship()
    assert actual.x == 0
    assert actual.y == 0


def test_ship_should_have_heading():
    sut = seafarers.Ship()
    assert sut.heading == 0


HEADING_DATA = [
    (1.5, 1.5),
    (360, 0),
    (-1, 359),
]


@pytest.mark.parametrize("given_heading, expected_heading", HEADING_DATA)
def test_ship_should_set_heading_with_limits(given_heading, expected_heading):
    sut = seafarers.Ship()
    sut.set_heading(given_heading)
    actual_heading = sut.heading
    assert actual_heading == expected_heading


def test_ship_should_have_speed():
    sut = seafarers.Ship()
    assert sut.speed == 1


@pytest.mark.parametrize("given_speed, expected_speed", [(0, 0), (-1, 0), (2, 1)])
def test_ship_should_set_speed_with_limits(given_speed, expected_speed):
    sut = seafarers.Ship()
    sut.set_speed(given_speed)
    actual_speed = sut.speed
    assert actual_speed == expected_speed


@pytest.mark.parametrize("given_speed, given_heading, expected_x, expected_y", [
    (1, 0, 0, 1),
    (1, 90, 1, 6.123233995736766e-17)])
def test_ship_should_move_according_to_heading_and_speed(given_speed, given_heading, expected_x, expected_y):
    sut = seafarers.Ship()
    sut.set_heading(given_heading)
    sut.set_speed(given_speed)
    sut.move()
    assert sut.x == expected_x
    assert sut.y == expected_y


def test_island_should_exist():
    given_x = 1
    given_y = 2
    sut = seafarers.Island(given_x, given_y)
    assert sut.x == given_x
    assert sut.y == given_y


@pytest.mark.parametrize("island_x, island_y, expected_visibility", [
    (0, 0, True),
    (11, 0, False),
])
def test_ship_should_determine_island_visibility(island_x, island_y, expected_visibility):
    sut = seafarers.Ship()
    island = seafarers.Island(island_x, island_y)
    actual = sut.can_see(island)
    assert actual == expected_visibility


@pytest.mark.parametrize("island_x, island_y, expected_dockworthiness", [
    (0, 0, True),
    (2, 0, False),
])
def test_ship_can_dock_with_island(island_x, island_y, expected_dockworthiness):
    sut = seafarers.Ship()
    island = seafarers.Island(island_x, island_y)
    actual = sut.can_dock(island)
    assert actual == expected_dockworthiness

def test_ship_when_docked_cannot_move():
    sut = seafarers.Ship()
    island = seafarers.Island(0, 0)
    sut.dock(island)
    sut.move()
    assert sut.x == 0
    assert sut.y == 0
