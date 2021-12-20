class Articles:
    def __init__(self):
        self._select_books = []  # Libros seleccionados
        self._amount_books = 0  # Cantidad de libros seleccionados
        self._types_of_books = 7  # Tipos posibles de libros

    def set_books(self, *args):
        """
        Fija la selección entrante de libros
        """
        for i in args:
            self._select_books.append(i)

    def set_amount_books_selected(self):
        """
        Cantidad de libros seleccionados
        """
        self._amount_books = len(self._select_books)

    def get_books(self):
        return self._select_books


class ShoppingBasket(Articles):

    def __init__(self):
        super().__init__()
        self._shopping_basket = [0, 0, 0, 0, 0, 0, 0]  # Cesta de la compra
        self._distinct_books = 0  # Tipos de libros en cesta
        self._unaccounted_books = self._amount_books  # Libros no contados
        self._first_price = 8  # Valor de cada libro
        self._discount_list = [0, 5, 10, 20, 25, 40, 50]  # Lista de descuentos
        self._price_without_discount = 0  # Precio sin descuento
        self._price_with_discount = 0  # Precio con descuento

    def set_shopping_basket(self):
        """
        Ordena por cantidad de libros
        """
        for i in self._select_books:
            self._shopping_basket[i - 1] += 1

    def set_distinct_books(self):
        """
        Fija cuantos libros distintos hay en la cesta
        """
        self._distinct_books = self._types_of_books - self._shopping_basket.count(0)

    def set_processed_books(self):
        """
        Contabiliza los libros procesados
        """
        self._unaccounted_books = sum(self._shopping_basket)

    def get_shopping_basket(self):
        return self._shopping_basket

    def get_regular_price(self):
        return sum(self._shopping_basket) * self._first_price

    def get_discount(self):
        return self._price_without_discount - self._price_with_discount

    def get_price_with_discount(self):
        result = 0
        while self._unaccounted_books > 0:
            result += self._distinct_books * self._first_price * (
                    1 - self._discount_list[self._distinct_books - 1] / 100)
            self._shopping_basket = [0 if x <= 0 else x - 1 for x in self._shopping_basket]
            self.set_distinct_books()
            self.set_processed_books()
        return result

    def get_core_method(self):
        self.set_amount_books_selected()
        self.set_shopping_basket()
        self.set_distinct_books()
        self.set_processed_books()
        return self.get_price_with_discount()

    def get_ticket(self):
        pass
        # TODO: terminar la opción de ticket
