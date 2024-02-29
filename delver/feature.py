import  inventory


class Feature:
    def __init__(self):
        self.room = None
        self.inventory = inventory.Inventory()

    def get_inventory(self):
        return self.inventory
