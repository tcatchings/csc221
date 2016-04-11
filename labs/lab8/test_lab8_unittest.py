import unittest
from lab8 import count_letters

class testCountLetters(unittest.TestCase):

    def setUp(self):
        pass

    def test_hello(self):
        self.assertEqual( count_letters('hello', 'l'), 2)

    def test_well(self):
        self.assertEqual( count_letters('well', 'e'), 1)

    def test_zero(self):
        self.assertEqual( count_letters('zero', 'x'), 0)

from lab8 import reverse_string

class testReverseString(unittest.TestCase):

    def setUp(self):
        pass

    def test_hola(self):
        self.assertEqual( reverse_string('hola'), 'aloh')

    def test_abba(self):
        self.assertEqual( reverse_string('abba'), 'abba')

from lab8 import is_palindrome

class testIsPalindrome(unittest.TestCase):

    def setUp(self):
        pass

    def test_oppo(self):
        self.assertTrue( is_palindrome('oppo'), True)

    def test_notapalindrome(self):
        self.assertFalse( is_palindrome('notapalindrome'), False)

from lab8 import match_ends

class testMatchEnds(unittest.TestCase):

    def setUp(self):
        pass

    def test_first_end(self):
        self.assertEqual( match_ends(['yup', 'aa', 'no']), 1)

    def test_second_end(self):
        self.assertEqual( match_ends(['hah', 'lol', 'pop']), 3)

    def test_third_end(self):
        self.assertEqual( match_ends(['should', 'return', 'zero']), 0)

from lab8 import front_x

class testFirstX(unittest.TestCase):

    def setUp(self):
        pass

    def test_first_list(self):
        self.assertEqual( front_x(['x', 'string', 'lab', 'xtra', 'zx']),
        ['x', 'xtra', 'string', 'lab', 'z'])

    def test_second_list(self):
        self.assertEqual( front_x(['apple', 'xbox', 'one', 'xox']),
        ['xbox', 'xox', 'apple', 'one'])

from lab8 import sort_last

class testSortLast(unittest.TestCase):

    def setUp(self):
        pass

    def test_first_tuple(self):
        self.assertEqual( sort_last([(1,4), (7,2), (2,3), (6, 6, 5)]),
        [(7,2), (2,3), (1,4), (6,6,5)])

    def test_second_tuple(self):
        self.assertEqual( sort_last([(9.9), (1123123, 1), (73, 8), (35, 5)]),
        [(1123123, 1), (35, 5), (73, 8), (9, 9)])

if __name__ == '__main__':
    unittest.main()


