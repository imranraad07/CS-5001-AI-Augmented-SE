import math

def sum_of_odd_factors(n):
    """Calculate the sum of all odd factors of a given number n."""
    result = 1
    # Remove all factors of 2 (even factors)
    while n % 2 == 0:
        n = n // 2

    # Check for odd factors starting from 3 up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        count = 0
        current_sum = 1
        current_term = 1
        while n % i == 0:
            count += 1
            n = n // i
            current_term *= i
            current_sum += current_term
        result *= current_sum

    # If remaining n is a prime number greater than 2
    if n > 2:
        result *= (1 + n)

    return result
