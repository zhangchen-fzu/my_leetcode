def coinChange(coins, amount):
    dp = [0] + [amount + 1] * (amount)
    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    return dp[-1] if dp[-1] != amount + 1 else -1












def coinChange1(coins, amount):
    dp = [0] + [amount + 1] * amount
    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if i - coins[j] >= 0:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    return dp[-1] if dp[-1] != amount + 1 else -1










