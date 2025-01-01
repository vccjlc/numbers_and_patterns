def partitions_optimized(n):
    """
    Returns the total number of partitions of n using an optimized iterative approach.
    """
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: 1 way to partition 0

    # Fill the dp array
    for k in range(1, n + 1):  # Iterate over part sizes
        for i in range(k, n + 1):  # Update dp array for all target values >= k
            dp[i] += dp[i - k]

    return dp[n]


if __name__ == "__main__":
    for i in range(1, 1000):
        print(f"Number of partitions of {i} = {partitions_optimized(i)}")
