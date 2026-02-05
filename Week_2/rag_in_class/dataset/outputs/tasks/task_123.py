def amicable_numbers_sum(limit):
    if not isinstance(limit, int):
        return "Input is not an integer!"
    if limit < 1:
        return "Input must be bigger than 0!"

    def sum_proper_divisors(n):
        return sum(fact for fact in range(1, n) if n % fact == 0)

    amicables = set()
    for num in range(2, limit + 1):
        if num in amicables:
            continue
        sum_fact = sum_proper_divisors(num)
        sum_fact2 = sum_proper_divisors(sum_fact)
        if num == sum_fact2 and num != sum_fact:
            amicables.update({num, sum_fact2})
    return sum(amicables)
