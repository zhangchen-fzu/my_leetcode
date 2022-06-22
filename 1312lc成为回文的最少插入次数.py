def minInsertions(s):
    m = len(s)
    dp = [[0] * (m) for _ in range(m)]
    for i in range(m - 1, -1, -1):
        for j in range(i + 1, m):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
    return dp[0][m -1]


def minInsertions1(s):
    m = len(s)
    dp = [0] * m
    for i in range(m - 1, -1, -1):
        left_top = 0
        for j in range(i + 1, m):
            tmp = dp[j]
            if s[i] == s[j]:
                dp[j] = left_top
            else:
                dp[j] = min(dp[j], dp[j - 1]) + 1
            left_top = tmp
    return dp[-1]