def min_cost(cost, m, n):
    """Calculate the minimum cost path from top-left to bottom-right of a cost matrix.

    Args:
        cost: 2D list representing the cost matrix
        m: row index of the destination cell
        n: column index of the destination cell

    Returns:
        Minimum cost to reach cell (m, n) from (0, 0)
    """
    # Initialize a DP table with the same dimensions as the cost matrix
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Base case: starting cell cost
    dp[0][0] = cost[0][0]

    # Fill first column (only one way to reach these cells)
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + cost[i][0]

    # Fill first row (only one way to reach these cells)
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + cost[0][j]

    # Fill the rest of the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + cost[i][j]

    return dp[m][n]
