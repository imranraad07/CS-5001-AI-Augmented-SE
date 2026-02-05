def get_max_sum(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = max(i, dp[i // 2] + dp[i // 3] + dp[i // 4] + dp[i // 5])

    return dp[n]
