class ShoppingCart:

    def __init__(self, **options):
        self.options = options
        self.items = []

    def add_to_cart(self, *items):
        self.items.extend(items)


cart = ShoppingCart(currency='USD') # BEAUTIFUL IS BETTER THAN UGLY

print(cart.options)
