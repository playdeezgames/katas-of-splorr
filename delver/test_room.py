import pytest
import room
import character

def test_room_exists():
    sut = room.Room()
    assert not sut.has_exit(character.NORTH)
    assert not sut.has_exit(character.EAST)
    assert not sut.has_exit(character.SOUTH)
    assert not sut.has_exit(character.WEST)