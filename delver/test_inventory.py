import inventory


def test_inventory_exists():
    my_inventory = inventory.Inventory()
    assert my_inventory is not None