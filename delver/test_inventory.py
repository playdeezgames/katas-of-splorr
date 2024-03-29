import inventory
import item


def test_inventory_exists():
    sut = inventory.Inventory()
    assert sut is not None


def test_inventory_starts_with_no_items():
    sut = inventory.Inventory()
    assert sut.is_empty()


def test_inventory_when_empty_does_not_contain_given_item():
    sut = inventory.Inventory()
    my_item = item.Item()
    assert not sut.contains_item(my_item)


def test_inventory_can_add_item():
    sut = inventory.Inventory()
    my_item = item.Item()
    sut.add_item(my_item)
    assert sut.contains_item(my_item)
    assert not sut.is_empty()


def test_inventory_can_add_item_only_once():
    sut = inventory.Inventory()
    my_item = item.Item()
    sut.add_item(my_item)
    sut.add_item(my_item)
    assert len(sut.items) == 1


def test_inventory_can_remove_item():
    sut = inventory.Inventory()
    my_item = item.Item()
    sut.add_item(my_item)
    sut.remove_item(my_item)
    assert not sut.contains_item(my_item)
    assert sut.is_empty()
