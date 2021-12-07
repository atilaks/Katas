class Articles:
    def __init__(self):
        self._select_books = []
        self._amount_books = 0
        self._types_of_books = 5

    def get_books(self):
        return self._select_books

    def set_books(self, *args):
        for i in args:
            self._select_books.append(i)

    def set_amount_books_selected(self):
        self._amount_books = len(self._select_books)


class ShoppingBasket(Articles):

    def __init__(self):
        super().__init__()
        self._shopping_basket = [0, 0, 0, 0, 0]
        self._price_without_discount = 0
        self._price_with_discount = 0
        self._first_price = 8
        self._discount_list = [0, 5, 10, 20, 25]
        self._sets = 0

    def set_shopping_basket(self):
        for i in self._select_books:
            self._shopping_basket[i - 1] += 1

    def get_shopping_basket(self):
        return self._shopping_basket

    def get_regular_price(self):
        return len(self._select_books) * self._first_price

    def get_discount(self):
        return self._price_without_discount - self._price_with_discount

    def set_distinct_books(self):
        self._sets = self._types_of_books - self._shopping_basket.count(0)

    def get_price_with_discount(self):
        while self._amount_books > 0:
            # result += self.
            pass

    def get_core_method(self, *args):
        pass

    def get_ticket(self):
        pass
