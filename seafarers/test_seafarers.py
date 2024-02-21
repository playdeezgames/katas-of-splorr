import pytest

import seafarers


def test_ship_should_have_xy():
    sut = seafarers.Ship()
    assert sut.x == 0
    assert sut.y == 0


def test_ship_should_have_heading():
    sut = seafarers.Ship()
    assert sut.heading == 0


@pytest.mark.parametrize("given_heading, expected_heading", [(32, 0), (33, 1), (-1, 31)])
def test_ship_should_set_heading(given_heading, expected_heading):
    sut = seafarers.Ship()
    sut.set_heading(given_heading)
    assert sut.heading == expected_heading

def test_ship_should_have_speed():
    sut = seafarers.Ship()
    assert sut.speed == 1


@pytest.mark.parametrize("given_speed, expected_speed", [(0, 0), (2, 1), (-1, 0)])
def test_ship_should_test_speed(given_speed, expected_speed):
    sut = seafarers.Ship()
    sut.set_speed(given_speed)
    assert sut.speed == expected_speed


@pytest.mark.parametrize("given_heading, expected_x, expected_y", [
    (0, 0, 1),
    (1, 0.1951, 0.9808),
    (27, -0.8315, 0.5556),
    ])
def test_ship_should_move(given_heading, expected_x, expected_y):
    sut = seafarers.Ship()
    sut.set_heading(given_heading)
    sut.move()
    assert sut.x == expected_x
    assert sut.y == expected_y
