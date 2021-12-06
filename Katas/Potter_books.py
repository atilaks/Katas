class Articles:
    def __init__(self):
        self._select_books = []

    def get_books(self):
        return self._select_books

    def set_books(self, *args):
        for i in args:
            self._select_books.append(i)


class Price:
    pass


class ShoppingBasket(Articles, Price):
    def __init__(self):
        super().__init__()
        self._shopping_basket = [0, 0, 0, 0, 0]

    def set_shopping_basket(self):
        for i in self._select_books:
            self._shopping_basket[i - 1] += 1

    def get_shopping_basket(self):
        return self._shopping_basket
