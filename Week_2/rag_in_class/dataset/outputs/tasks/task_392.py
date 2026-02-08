def get_max_sum(n):
    # Initialize the result list with base cases
    res = [0, 1]

    # Iterate from 2 to n (inclusive)
    for i in range(2, n + 1):
        # Calculate the maximum sum for current index
        current_max = max(
            i,
            res[i // 2] + res[i // 3] + res[i // 4] + res[i // 5]
        )
        res.append(current_max)

    return res[n]
