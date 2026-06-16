from numb3rs import validate


def test_valid_ips():
    """Test standard valid IPv4 addresses."""
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True
    assert validate("0.0.0.0") is True
    assert validate("192.168.1.1") is True


def test_invalid_ranges():
    """Test addresses where numbers exceed 255 in different positions."""
    assert validate("275.3.6.28") is False      # First byte out of range (The NUMB3RS case)
    assert validate("127.300.6.28") is False    # Second byte out of range
    assert validate("127.3.512.28") is False    # Third byte out of range
    assert validate("127.3.6.1000") is False    # Fourth byte out of range


def test_invalid_formats():
    """Test non-numeric strings, leading zeros, and incorrect lengths."""
    assert validate("cat") is False
    assert validate("192.168.001.1") is False   # Forbidden leading zeros
    assert validate("192.168.1") is False       # Too few octets
    assert validate("192.168.1.1.1") is False   # Too many octets
    assert validate("192.168.1.a") is False     # Contains letters
