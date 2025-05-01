import pytest
from problems import reverse_string, find_max, is_palindrome

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("A") == "A"

def test_find_max():
    assert find_max([1, 5, 3, 9]) == 9
    assert find_max([-1, -5, -3, -9]) == -1
    assert find_max([]) == None

def test_is_palindrome():
    assert is_palindrome("racecar")
    assert not is_palindrome("hello")
    assert is_palindrome("") == True
    assert is_palindrome("Racecar")
    assert is_palindrome("") == True
    assert is_palindrome("A man, a plan, a canal: Panama.")