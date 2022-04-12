import unittest


class GiftNotDefinedException(Exception):
    pass


class Gift:
    def process(self):
        raise GiftNotDefinedException("Gift is not defined")


class Book(Gift):
    def __init__(self, title):
        self.name = title

    def process(self):
        return "Duplicated packing slip for shipping"


class Physical(Gift):
    def __init__(self, name):
        self.name = name

    def process(self):
        return "Packing slip for shipping"


class Christmatizator:
    def process(self, gift):
        result = gift.process()
        return result


class test_christmas_kata(unittest.TestCase):
    def test_gift_is_physical_generates_packing_slip(self):
        # Arrange
        christmatizator = Christmatizator()
        expected = "Packing slip for shipping"
        gift = Physical("Playstation 2")

        # Act
        result = christmatizator.process(gift)

        # Assert
        self.assertEqual(expected, result)

    def test_gift_is_a_book_generates_duplicated_packing_slip(self):
        # Arrange
        christmatizator = Christmatizator()
        expected = "Duplicated packing slip for shipping"
        gift = Book("Harry Potter")

        # Act
        result = christmatizator.process(gift)

        # Assert
        self.assertEqual(expected, result)

    def test_gift_can_be_processed(self):
        # Arrange
        gift = Gift()

        # Act

        # Assert
        self.assertRaises(GiftNotDefinedException, lambda: gift.process())


if __name__ == "__main__":
    unittest.main()