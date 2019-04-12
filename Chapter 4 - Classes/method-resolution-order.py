# Method Resolution Order (MRO)
# from left to right, in the order the classes were defined as base classes
# Python uses an algorithm called C3


class Book:
    def __init__(self, title):
        self.title = title
        self.page = 1

    def read(self):
        return 'There sure are a lot of words on page %s.' % self.page

    def bookmark(self, page):
        self.page = page


class Novel(Book):
    pass


class Mystery(Novel):
    def read(self):
        return "Page %s and I still don't know who did it!" % self.page


book1 = Book('Pro Python')
print(book1.read())

book1.bookmark(page=52)
print(book1.read())

book2 = Novel('Pride and Prejudice')
print(book2.read())

book3 = Mystery('Murder on the Orient Express')
print(book3.read())

book3.bookmark(page=352)
print(book3.read())


class Product:
    def purchase(self):
        return 'Wow, you must really like it!'


class BookProduct(Book, Product):
    pass


class MysteryProduct(Mystery, Product):
    def purchase(self):
        return 'Whodunnit?'


product1 = BookProduct('Pro Python')
print(product1.purchase())

product2 = MysteryProduct('Murder on the Orient Express')
print(product2.purchase())


class A:
    def test(self):
        return 'A'


class B(A):
    pass


class C:
    def test(self):
        return 'C'


class D(B, C):
    pass


print(D().test())  # A


class D(C, B):
    pass


print(D().test())  # C

