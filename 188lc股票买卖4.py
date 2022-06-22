'''
#############################################################################################################
**题目188：（数组）
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
**示例：
输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
**条件：
0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
#############################################################################################################
'''
'''
动规方法1：
与k=2时方法一样：
dp定义：dp[U][V][k]为第U天还剩V次交易机会，目前持股状态为k
状态转移方程：
            dp[u][v][0] = max(dp[u - 1][v][0], dp[u - 1][v][1] + prices[u - 1])
            dp[u][v][1] = max(dp[u - 1][v][1], dp[u - 1][v - 1][0] - prices[u - 1])
base case:
        dp[i][0][0] = 0
        dp[i][0][1] = -float('inf')
        dp[0][j][0] = 0
        dp[0][j][1] = -float('inf')
复杂度分析:
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution1(object):
    def maxProfit(self, k, prices):
        m = len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0][0] = 0
            dp[i][0][1] = -float('inf')
        for j in range(1, k + 1):
            dp[0][j][0] = 0
            dp[0][j][1] = -float('inf')
        for u in range(1, m + 1):
            for v in range(1, k + 1):
                dp[u][v][0] = max(dp[u - 1][v][0], dp[u - 1][v][1] + prices[u - 1])
                dp[u][v][1] = max(dp[u - 1][v][1], dp[u - 1][v - 1][0] - prices[u - 1])
        return dp[m][k][0]

'''
动规优化：
k无法获取是多少，但是在实际买卖中k最多是len(prices)/2次，所以当k在[0:len(prices)/2]之内时，最终结果与k有关；
当k在[len(prices)/2:inf]时，最终结果与k无关了，k可看做是无穷大。（122 & 123题的结合）
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution2(object):
    def maxProfit(self, k, prices):
        m = len(prices)
        mid_len = m // 2
        if k > mid_len:
            dp=[[0] * 2 for _ in range(m + 1)]
            dp[0][1] = -float('inf')
            for i in range(m):
                dp[i + 1][0] = max(dp[i][0], dp[i][1] + prices[i])
                dp[i + 1][1] = max(dp[i][1], dp[i][0] - prices[i])
            return dp[m][0]
        else:
            dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(m + 1)]
            for i in range(m + 1):
                dp[i][0][0] = 0
                dp[i][0][1] = -float('inf')
            for j in range(1, k + 1):
                dp[0][j][0] = 0
                dp[0][j][1] = -float('inf')
            for u in range(1, m + 1):
                for v in range(1, k + 1):
                    dp[u][v][0] = max(dp[u - 1][v][0], dp[u - 1][v][1] + prices[u - 1])
                    dp[u][v][1] = max(dp[u - 1][v][1], dp[u - 1][v - 1][0] - prices[u - 1])
            return dp[m][k][0]








def maxProfit(k, prices):
    m = len(prices)
    dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0][0] = 0
        dp[i][0][1] = -float('inf')

    for j in range(k + 1):
        dp[0][j][0] = 0
        dp[0][j][1] = -float('inf')

    for i in range(1, m + 1):
        for j in range(1, k + 1):
            dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])
            dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i - 1])
    return  dp[m][k][0]

