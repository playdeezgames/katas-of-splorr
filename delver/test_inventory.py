import inventory


def test_inventory_exists():
    sut = inventory.Inventory()
    assert sut is not None


def test_inventory_starts_with_no_items():
    sut = inventory.Inventory()
    assert len(sut.items) == 0
