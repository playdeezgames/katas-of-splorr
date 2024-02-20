import seafarers


def test_ship_should_have_xy():
    actual = seafarers.Ship()
    assert actual.x == 0
    assert actual.y == 0


def test_ship_should_have_heading():
    sut = seafarers.Ship()
    assert sut.heading == 0
