import unittest

from example import get_message


class ExampleTest(unittest.TestCase):
    def test1(self):
        """
        Tests that get_message() returns a string.
        """
        # Arrange
        very_big_number = 2001

        self.assert_get_message_returns_string(very_big_number)

    def test2(self):
        """
        Tests that get_message() returns a string.
        """
        # Arrange
        very_small_number = 1999

        self.assert_get_message_returns_string(very_small_number)

    def test3(self):
        """
        Tests that get_message() returns a string.
        """
        # Arrange
        exactly_2000 = 2000

        self.assert_get_message_returns_string(exactly_2000)

    def assert_get_message_returns_string(self, value: int):
        # Act
        result = get_message(value)

        # Assert
        self.assertIsInstance(result, str)
