from lab8 import count_letters

def test_hello():
    assert count_letters('hello', 'l') == 2

def test_zero():
    assert count_letters('zero', 'x') == 0

from lab8 import reverse_string

def test_hola():
    assert reverse_string('hola') == 'aloh'

def test_abba():
    assert reverse_string('abba') == 'abba'

from lab8 import is_palindrome

def test_oppo():
    assert is_palindrome('oppo') == True

def test_notapalindrome():
    assert is_palindrome('notapalindrome') == False

from lab8 import front_x

def test_first_list():
    assert front_x(
        ['x', 'string', 'lab', 'xtra', 'zx']
        ) == ['x', 'xtra', 'string', 'lab', 'z']

def test_second_list():
    assert front_x(
        ['apple', 'xbox', 'one', 'xox']
        ) == ['xbox', 'xox', 'apple', 'one']

from lab8 import sort_last

def test_first_tuple():
    assert sort_last(
        [(1,4), (7,2), (2,3), (6, 6, 5)]
        ) == [(7,2), (2,3), (1,4), (6,6,5)]

def test_second_tuple():
    assert sort_last(
        [(9.9), (1123123, 1), (73, 8), (35, 5)]
        ) == [(1123123, 1), (35, 5), (73, 8), (9, 9)]
