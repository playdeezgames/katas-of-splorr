import pytest
import item


def test_item_exists():
    my_item = item.Item()
    assert my_item is not None
