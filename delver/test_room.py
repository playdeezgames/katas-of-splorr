import pytest
import room
import direction


def test_room_exists():
    sut = room.Room()
    assert not sut.has_exit(direction.NORTH)
    assert not sut.has_exit(direction.EAST)
    assert not sut.has_exit(direction.SOUTH)
    assert not sut.has_exit(direction.WEST)