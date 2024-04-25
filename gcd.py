def gcd(a, b):
    """Calculate the Greatest Common Divisor (GCD) of two integers using Euclid's algorithm.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The GCD of a and b.

    Raises:
        ValueError: If both a and b are 0, or if either a or b is negative.
    """
    if a < 0 or b < 0:
        raise ValueError("GCD is not defined for negative numbers.")
    if a == 0 and b == 0:
        raise ValueError("GCD is not defined when both a and b are 0.")
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b % a, a)


# Example usage:
try:
    print(gcd(48, 18))  # Should print 6
    print(gcd(-10, 5))  # Should raise an exception
except ValueError as e:
    print(e)
