import feature
import room


def test_feature_exists():
    sut = feature.Feature()
    assert sut is not None


def test_feature_aware_of_room():
    sut = feature.Feature()
    my_room = room.Room()
    my_room.add_feature(sut)
    assert sut.room == my_room
