import pytest

import seafarers


def test_ship_should_have_xy():
    actual = seafarers.Ship()
    assert actual.x == 0
    assert actual.y == 0


def test_ship_should_have_heading():
    sut = seafarers.Ship()
    assert sut.heading == 0


@pytest.mark.parametrize("given_heading, expected_heading",[(1,1)])
def test_ship_should_set_heading_with_limits(given_heading, expected_heading):
    sut = seafarers.Ship()
    sut.set_heading(given_heading)
    actual_heading = sut.heading
    assert actual_heading == expected_heading

