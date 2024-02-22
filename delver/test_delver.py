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
