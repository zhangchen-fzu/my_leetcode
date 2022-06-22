def change(amount, coins):
    m = len(coins)
    dp = [[0] * (amount + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, amount + 1):
            if j - coins[i - 1] >= 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][amount]













def change(amount, coins):
    m = len(coins)
    dp = [[0] * (amount + 1) for _ in range(m + 1)]

    for i in range(1, amount + 1):
        dp[0][i] = 0
    for j in range(m + 1):
        dp[j][0] = 1

    for i in range(1, m + 1):
        for j in range(1, amount + 1):
            if j - coins[i - 1] >= 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][amount]



def change1(amount, coins):
    m = len(coins)
    dp = [1] + [0] * amount
    for i in range(m):
        for j in range(amount + 1):
            if j - coins[i] >= 0:
                dp[j] = dp[j] + dp[j - coins[i]]

    return dp[-1]












