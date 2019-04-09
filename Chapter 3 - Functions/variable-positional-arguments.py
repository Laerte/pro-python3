class ShoppingCart:

    items = []

    def add_to_cart(self, *items):
        self.items.extend(items)


cart = ShoppingCart()

cart.add_to_cart({'name': 'Product 1'})

print(cart.items)

cart.add_to_cart({'name': 'Product 2'},
                 {'name': 'Product 3'})

print(cart.items)
