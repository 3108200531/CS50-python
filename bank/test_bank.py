from bank import value

def test_blank_value():
    assert value("") == 100
    assert value("what's up? ") == 100

def test_hello_value():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello") == 0


def test_h_value():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("how are you?") == 20


