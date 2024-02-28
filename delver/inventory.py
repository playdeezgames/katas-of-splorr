class Inventory:
    def __init__(self):
        self.items = []

    def contains_item(self, item):
        return item in self.items

    def add_item(self, item):
        if not self.contains_item(item):
            self.items.append(item)

    def remove_item(self, item):
        self.items = [i for i in self.items if i != item]

    def is_empty(self):
        return len(self.items) == 0
