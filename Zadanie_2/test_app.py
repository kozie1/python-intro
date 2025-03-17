# test_app.py

import unittest
from app import *

class TestApp(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("12345"), "54321")

    def test_get_max_value(self):
        self.assertEqual(get_max_value([1, 2, 3, 4]), 4)
        self.assertEqual(get_max_value([-5, -2, -10]), -2)
        with self.assertRaises(ValueError):
            get_max_value([])

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(1), 1)
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_count_words(self):
        self.assertEqual(count_words("Hello world"), 2)
        self.assertEqual(count_words("One two three four"), 4)
        self.assertEqual(count_words(""), 0)

    def test_is_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("Dormitory", "Dirtyroom"))
        self.assertFalse(is_anagram("Python", "Java"))

if __name__ == "__main__":
    unittest.main()

