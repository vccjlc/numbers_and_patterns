from collections import Counter

def prime_factors(n):
    """Calculate the prime factors of a given number 'n' using a Counter to store factors directly."""
    factors = Counter()  # Initialize an empty Counter for the factors

    # Check for number of 2s that divide n
    while n % 2 == 0:
        factors[2] += 1
        n = n // 2  # Divide n by 2 until it is no longer even

    # Check for odd factors from 3 up to the square root of n
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors[i] += 1
            n = n // i  # Divide n by i until it is no longer divisible by i

    # If n is still greater than 2 after all divisions, it is a prime number
    if n > 2:
        factors[n] += 1

    return factors

def lcm(a, b):
    """Calculate the least common multiple (LCM) of two numbers 'a' and 'b' using their prime factorization."""
    count_a = prime_factors(a)
    count_b = prime_factors(b)
    print(count_a)  # Debug: Print prime factors of a
    print(count_b)  # Debug: Print prime factors of b

    result = 1
    all_keys = set(count_a) | set(count_b)  # Combine all prime factors from both numbers

    # Compute LCM by taking the highest power of all encountered prime factors
    for key in all_keys:
        max_count = max(count_a.get(key, 0), count_b.get(key, 0))
        result *= key ** max_count

    print(result)  # Debug: Print the final result
    return result

# Testing the LCM calculation
lcm(142131412, 4253511)
