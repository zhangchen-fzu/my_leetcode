'''
#############################################################################################################
**题目215：（数组）
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
**示例：
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
**条件：
1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
#############################################################################################################
'''

'''
动规方法：
dp定义：dp[i][j]为从开始到grid[i][j]的最小路径和
状态转移方程：dp[i][j]由上及左侧的最小值加上grid[i][j]构成
base case:第一行及第一列的值需提前处理好
复杂度分析：
时间复杂度：O(M*N)
空间复杂度：O(M*N)

'''
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * (n) for _ in range(m)]

        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])
        return dp[m - 1][n - 1]

'''
动规优化：
在源grid上修改
复杂度分析：
时间复杂度：O(M*N)
空间复杂度：O(1)
'''
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        for i in range(1, m):
            grid[i][0] = grid[i - 1][0] + grid[i][0]
        for j in range(1, n):
            grid[0][j] = grid[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i - 1][j] + grid[i][j], grid[i][j - 1] + grid[i][j])
        return grid[m - 1][n - 1]






def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]


def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1, m):
        grid[i][0] = grid[i - 1][0] + grid[i][0]
    for j in range(1, n):
        grid[0][j] = grid[0][j - 1] + grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
    return grid[m - 1][n - 1]













