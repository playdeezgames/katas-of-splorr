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
