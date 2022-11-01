import unittest

from example import get_message


class ExampleTest(unittest.TestCase):
    def test1(self):
        """
        Tests that get_message() returns a string.
        """
        result = get_message(6316723)

        self.assertIsInstance(result, str)
