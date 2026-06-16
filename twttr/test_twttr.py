from twttr import shorten

def test_shorten():
    assert shorten("hello, world") == "hll, wrld"

def test_no_vowels():
    assert shorten("aeiou") == ""

def test_uppercase():
    assert shorten("HELLO") == "HLL"

def test_numbers_and_punctuation():
    assert shorten("CS50!") == "CS50!"
