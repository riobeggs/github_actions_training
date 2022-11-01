import unittest

from example import get_message


class ExampleTest(unittest.TestCase):
    def test1(self):
        """
        Tests that get_message() returns a string.
        """
        # Arrange
        very_big_number = 2001

        # Act
        result = get_message(very_big_number)

        # Assert
        self.assertIsInstance(result, str)

    def test2(self):
        """
        Tests that get_message() returns a string.
        """
        # Arrange
        very_small_number = 1999

        # Act
        result = get_message(very_small_number)

        # Assert
        self.assertIsInstance(result, str)

    def test3(self):
        """
        Tests that get_message() returns a string.
        """
        # Arrange
        exactly_2000 = 2000

        # Act
        result = get_message(exactly_2000)

        # Assert
        self.assertIsInstance(result, str)
