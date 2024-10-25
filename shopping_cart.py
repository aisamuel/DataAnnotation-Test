class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item not in self.items:
            raise ValueError("Item not in cart")
        self.items.remove(item)

    def total_price(self):
        return sum(item.price for item in self.items)

    def clear_cart(self):
        self.items = []

    def __len__(self):
        return len(self.items)