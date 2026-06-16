import pytest
from working import convert


def test_valid_conversions_without_minutes():
    """Test standard valid conversions where minutes are omitted."""
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_valid_conversions_with_minutes():
    """Test standard valid conversions including exact minutes."""
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_mixed_valid_formats():
    """Test valid inputs that mix minutes formats (as stated in problem constraints)."""
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"


def test_invalid_times():
    """Test mathematical constraints (e.g. out of range minutes or hours)."""
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")


def test_invalid_formats():
    """Test structurally incorrect delimiters, missing spaces, or bad strings."""
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")  # Uses a dash instead of 'to'
    with pytest.raises(ValueError):
        convert("9AM to 5PM")   # Missing whitespace before period indicator
    with pytest.raises(ValueError):
        convert("cat")
