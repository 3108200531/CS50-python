import pytest
from fuel import convert, gauge

def test_convert_norm():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/1") == 100

def test_convert_error():
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
