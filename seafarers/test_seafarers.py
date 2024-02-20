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