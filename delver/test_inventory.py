import inventory


def test_inventory_exists():
    sut = inventory.Inventory()
    assert sut is not None
