testclass Jar:
    def _init_(self, capacity=12):
        # Initialize with the capacity and ensure it's a non-negative integer.
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._cookies = 0  # Initially, the number of cookies is 0.

    def _str_(self):
        # Return a string with as many "🍪" as the current number of cookies.
        return "🍪" * self._cookies

    def deposit(self, n):
        # Add 'n' cookies, but ensure we do not exceed capacity.
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self._cookies + n > self._capacity:
            raise ValueError("Cannot deposit cookies: exceeding capacity.")
        self._cookies += n

    def withdraw(self, n):
        # Remove 'n' cookies, but ensure there are enough cookies to withdraw.
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies.")
        if self._cookies < n:
            raise ValueError("Cannot withdraw cookies: not enough cookies.")
        self._cookies -= n

    @property
    def capacity(self):
        # Return the maximum capacity of the jar.
        return self._capacity

    @property
    def size(self):
        # Return the current number of cookies in the jar.
        return self._cookies
