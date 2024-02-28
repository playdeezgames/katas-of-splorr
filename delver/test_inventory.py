import inventory
import item


def test_inventory_exists():
    sut = inventory.Inventory()
    assert sut is not None


def test_inventory_starts_with_no_items():
    sut = inventory.Inventory()
    assert len(sut.items) == 0


def test_inventory_when_empty_does_not_contain_given_item():
    sut = inventory.Inventory()
    my_item = item.Item()
    assert not sut.contains_item(my_item)