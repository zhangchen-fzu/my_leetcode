class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1] * n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1 or (i > 0 and dp[i - 1][0] == 0):
                dp[i][0] = 0

        for j in range(n):
            if obstacleGrid[0][j] == 1 or (j > 0 and dp[0][j - 1] == 0):
                dp[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]







def uniquePathsWithObstacles1(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    dp = [[0] * n for _ in range(m)]
    for i in range(n):
        if obstacleGrid[0][i] == 1 or dp[0][i - 1] == 0:
            dp[0][i] = 0
        else:
            dp[0][i] = 1

    for j in range(m):
        if obstacleGrid[j][0] == 1 or dp[j - 1][0] == 0:
            dp[j][0] = 0
        else:
            dp[j][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp

print(uniquePathsWithObstacles1([[0,0,0],[0,1,0],[0,0,0]]))


























