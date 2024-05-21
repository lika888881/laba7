import unittest

from reverse import reverse


class TestReverse(unittest.TestCase):
    def test_with_empty_string(self):
        result = reverse('')

        self.assertEquals(result, '')

    def test_with_one_symbol_string(self):
        result = reverse('a')

        self.assertEquals(result, 'a')

    def test_with_palindrome(self):
        result = reverse('121')

        self.assertEquals(result, '121')

    def test_string(self):
        result = reverse('abcd')

        self.assertEquals(result, 'dcba')

    def test_with_not_string(self):
        with self.assertRaises(TypeError):
            reverse(123)

    def test_with_iterable(self):
        with self.assertRaises(TypeError):
            reverse([1, 2, 3])


if __name__ == '__main__':
    unittest.main()
