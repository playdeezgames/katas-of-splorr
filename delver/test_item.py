import pytest
import item


def test_item_exists():
    sut = item.Item()
    assert sut is not None
