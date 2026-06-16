import pytest
from plates import is_valid

def test_is_valid_length():
    assert is_valid("c") is False
    assert is_valid("medea1230") is False
    assert is_valid("med123") is True

def test_is_valid_digit_placement():
    assert is_valid("01c") is False
    assert is_valid("123med") is False
    assert is_valid("m12ed") is False
    assert is_valid("cs50") is True

def test_zero_placement():
    assert not is_valid("CS05")
    assert not is_valid("CS01")

def test_alphanumeric():
    assert not is_valid("CS-50")
    assert not is_valid("CS 50")

def test_beginning_letters():
    assert not is_valid("1A")
    assert not is_valid("A1")
    assert not is_valid("1CS50")
    assert is_valid("CS50")
    
def test_number_placement():
    assert not is_valid("CS5A")
    assert not is_valid("CS50A")
    assert is_valid("CS50")



