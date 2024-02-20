import pytest
import seafarers

def test_create_ship():
    actual = seafarers.Ship()
    assert actual.x == 0
    assert actual.y == 0
