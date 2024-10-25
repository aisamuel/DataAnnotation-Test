import pytest
import warnings
from shopping_cart import Item, ShoppingCart

class TestShoppingCart:
    @pytest.fixture
    def cart(self):
        return ShoppingCart()

    @pytest.fixture
    def item1(self):
        return Item(name="Laptop", price=1000)

    @pytest.fixture
    def item2(self):
        return Item(name="Mouse", price=50)

    def test_add_item(self, cart, item1, item2):
        warnings.warn("This function is deprecated.", DeprecationWarning)
        cart.add_item(item1)
        cart.add_item(item2)
        assert len(cart) == 2
        assert cart.items[0].name == "Laptop"
        assert cart.items[1].name == "Mouse"

    def verify_remove_item(self, cart, item1, item2):
        cart.add_item(item1)
        cart.add_item(item2)
        cart.remove_item(item1)
        assert len(cart) == 1
        assert cart.items[0].name == "Mouse"

    def verify_remove_item_not_in_cart(self):
        cart = ShoppingCart()
        item1 = Item(name="Laptop", price=1000)

        with pytest.raises(ValueError, match="Item not in cart"):
            cart.remove_item(item1)

    def test_clear_cart(self, cart, item1, item2):
        cart.add_item(item1)
        cart.add_item(item2)
        cart.clear_cart()
        assert len(cart) == 0

    @pytest.mark.parametrize(
        "items, expected_total",
        [
            ([], 0),
            ([Item(name="Book", price=30)], 30),
            ([Item(name="Monitor", price=200), Item(name="Keyboard", price=80)], 280),
        ],
    )
    def test_total_price(self, items, expected_total):
        cart = ShoppingCart()
        for item in items:
            cart.add_item(item)
        assert cart.total_price() == expected_total