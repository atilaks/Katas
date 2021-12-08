import unittest
from Potter_books import *


class PotterBooksTest(unittest.TestCase):
    def test_read_shopping_list(self):
        # Arrange
        article = ShoppingBasket()
        expected = [1]
        article.set_books(1)

        # Act
        result = article.get_books()

        # Assert
        self.assertEqual(result, expected)

    def test_read_shopping_list2(self):
        article = ShoppingBasket()
        expected = [1, 2, 3, 1, 3]
        article.set_books(1, 2, 3, 1, 3)

        result = article.get_books()

        self.assertEqual(result, expected)

    def test_shopping_basket(self):
        basket = ShoppingBasket()
        expected = [0, 2, 0, 1, 0, 0, 0]
        basket.set_books(4, 2, 2)
        basket.set_shopping_basket()

        result = basket.get_shopping_basket()

        self.assertEqual(result, expected)

    def test_regular_price_of_one_book(self):
        basket = ShoppingBasket()
        expected = 8
        basket.set_books(4)
        basket.set_shopping_basket()

        result = basket.get_regular_price()

        self.assertEqual(result, expected)

    def test_regular_price_of_any_amount_book(self):
        basket = ShoppingBasket()
        expected = 40
        basket.set_books(4, 5, 3, 5, 2)
        basket.set_shopping_basket()

        result = basket.get_regular_price()

        self.assertEqual(result, expected)

    def test_books_on_basket(self):
        basket = ShoppingBasket()
        expected = 4
        basket.set_books(1, 5, 3, 1)
        basket.set_amount_books_selected()

        result = basket._amount_books

        self.assertEqual(result, expected)

    def test_distinct_books_on_basket(self):
        basket = ShoppingBasket()
        expected = 2
        basket.set_books(1, 5, 1, 1)
        basket.set_shopping_basket()
        basket.set_distinct_books()

        result = basket._distinct_books

        self.assertEqual(result, expected)

    def test_price_with_5_percent_discount(self):
        basket = ShoppingBasket()
        expected = 15.2
        basket.set_books(1, 5)
        basket.set_amount_books_selected()
        basket.set_shopping_basket()
        basket.set_distinct_books()
        basket.set_processed_books()

        result = basket.get_price_with_discount()

        self.assertEqual(result, expected)

    def test_two_same_books(self):
        basket = ShoppingBasket()
        expected = 16
        basket.set_books(1, 1)
        basket.set_amount_books_selected()
        basket.set_shopping_basket()
        basket.set_distinct_books()
        basket.set_processed_books()

        result = basket.get_price_with_discount()

        self.assertEqual(result, expected)

    def test_core_calculator(self):
        basket = ShoppingBasket()
        expected = 16
        basket.set_books(1, 1)

        result = basket.get_core_method()

        self.assertEqual(result, expected)

    def test_3_different_books(self):
        basket = ShoppingBasket()
        expected = 29.6
        basket.set_books(1, 1, 3, 2)

        result = basket.get_core_method()

        self.assertEqual(result, expected)

    def test_any_combination(self):
        basket = ShoppingBasket()
        expected = 53.2
        basket.set_books(1, 1, 1, 2, 2, 3, 4, 5)

        result = basket.get_core_method()

        self.assertEqual(result, expected)

    def test_7_books(self):
        basket = ShoppingBasket()
        expected = 28
        basket.set_books(1, 2, 3, 4, 5, 6, 7)

        result = basket.get_core_method()

        self.assertEqual(result, expected)

    def test_random1(self):
        basket = ShoppingBasket()
        expected = 44
        basket.set_books(1, 2, 3, 4, 5, 6, 1, 6)

        result = basket.get_core_method()

        self.assertEqual(result, expected)

    def test_random2(self):
        basket = ShoppingBasket()
        expected = 29.6
        basket.set_books(7, 6, 5, 5)

        result = basket.get_core_method()

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
