from um import count


def test_isolated_um():
    """Test standard instances of 'um' with varying spaces and counts."""
    assert count("um") == 1
    assert count("um um") == 2
    assert count("  um  ") == 1


def test_case_insensitivity():
    assert count("Um, thanks for the help.") == 1
    assert count("UM, I don't know, uM, maybe?") == 2


def test_um_as_substring():
    assert count("yummy food") == 0
    assert count("this is an album") == 0
    assert count("clumsy umbrella") == 0
    # Combined check: an isolated "um" mixed with words containing "um"
    assert count("um, yummy album, um") == 2


def test_punctuation_boundaries():
    assert count("hello, um...") == 1
    assert count("um?") == 1
    assert count("(um)") == 1
