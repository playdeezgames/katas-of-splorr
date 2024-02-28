class Inventory:
    def __init__(self):
        self.items = []

    def contains_item(self, item):
        return item in self.items

    def add_item(self, item):
        self.items.append(item)
