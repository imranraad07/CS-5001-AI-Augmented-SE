import math

def sum_of_odd_Factors(n):
    res = 1
    # Remove all factors of 2
    while n % 2 == 0:
        n = n // 2

    # Check for odd factors from 3 to sqrt(n)
    for i in range(3, int(math.sqrt(n) + 1)):
        count = 0
        curr_sum = 1
        curr_term = 1
        # While i divides n, process the factor
        while n % i == 0:
            count += 1
            n = n // i
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum

    # If remaining n is a prime > 2
    if n >= 2:
        res *= (1 + n)

    return res
