def amicable_numbers_sum(limit):
    if not isinstance(limit, int):
        return "Input is not an integer!"
    if limit < 1:
        return "Input must be bigger than 0!"

    amicables = set()

    for num in range(2, limit + 1):
        if num in amicables:
            continue

        # Calculate sum of proper divisors for the current number
        sum_fact = sum(fact for fact in range(1, num) if num % fact == 0)

        # Calculate sum of proper divisors for the sum_fact
        sum_fact2 = sum(fact for fact in range(1, sum_fact) if sum_fact % fact == 0)

        # Check if the numbers form an amicable pair
        if num == sum_fact2 and num != sum_fact:
            amicables.add(num)
            amicables.add(sum_fact2)

    return sum(amicables)
