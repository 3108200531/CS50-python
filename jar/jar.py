class Jar:

    def __init__(self, capacity=12):
        # Validate that capacity is an integer and is non-negative
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # Cleanly prints 'n' number of cookie emojis
        return self._size * "🍪"

    def deposit(self, n):
        # Ensure we don't overfill the cookie jar
        if self._size + n > self._capacity:
            raise ValueError("Exceeds jar capacity")
        self._size += n

    def withdraw(self, n):
        # Ensure we aren't stealing cookies that don't exist
        if n > self._size:
            raise ValueError("Not enough cookies in the jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
