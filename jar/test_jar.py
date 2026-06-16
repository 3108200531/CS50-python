import pytest
from jar import Jar


def test_init():
    # Test valid initializations
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    custom_jar = Jar(5)
    assert custom_jar.capacity == 5

    # Test that invalid initializations correctly throw a ValueError
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("ten")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(5)
    assert jar.size == 10

    # Test trying to deposit past the maximum capacity limit
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(8)

    jar.withdraw(3)
    assert jar.size == 5

    jar.withdraw(5)
    assert jar.size == 0

    # Test trying to withdraw more cookies than are currently inside
    with pytest.raises(ValueError):
        jar.withdraw(1)
