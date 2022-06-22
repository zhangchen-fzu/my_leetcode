'''
#############################################################################################################
**题目123：（数组）
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
**示例：
输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
**条件：
1 <= prices.length <= 105
0 <= prices[i] <= 105
#############################################################################################################
'''
'''
动规方法：
dp定义：dp[i][j][k]为第i天还剩j次交易机会，目前持股状态为k
状态转移方程：dp[i][j][0]=max(dp[i-1][j][0],dp[i-1][j][1]+price[i])
            dp[i][j][1]=max(dp[i-1][j][1],dp[i-1][j-1][0]-price[i])
            其中，j为2，涉及到dp[i-1][1][0]，可通过两种方法得到，一种是循环计算；另外一种是一一列举
base case:  dp[i][0][0] = 0
            dp[i][0][1] = -float('inf')
            dp[0][j][0] = 0
            dp[0][j][1] = -float('inf')
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def maxProfit(self, prices):
        m = len(prices)
        dp = [[[0] * 2 for _ in range(2 + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0][0] = 0
            dp[i][0][1] = -float('inf')
        for j in range(1, 2 + 1):
            dp[0][j][0] = 0
            dp[0][j][1] = -float('inf')
        for k in range(1, m + 1):
            for m in range(1, 2 + 1):
                dp[k][m][0] = max(dp[k - 1][m][0], dp[k - 1][m][1] + prices[k - 1])
                dp[k][m][1] = max(dp[k - 1][m][1], dp[k - 1][m - 1][0] - prices[k - 1])
        return dp[m][2][0]

class Solution(object):
    def maxProfit(self, prices):
        m = len(prices)
        dp = [[[0] * 2 for _ in range(2 + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0][0] = 0
            dp[i][0][1] = -float('inf')
        for j in range(1, 2 + 1):
            dp[0][j][0] = 0
            dp[0][j][1] = -float('inf')
        for k in range(1, m + 1):
            dp[k][2][0] = max(dp[k - 1][2][0], dp[k - 1][2][1] + prices[k - 1])
            dp[k][2][1] = max(dp[k - 1][2][1], dp[k - 1][1][0] - prices[k - 1])
            dp[k][1][0] = max(dp[k - 1][1][0], dp[k - 1][1][1] + prices[k - 1])
            dp[k][1][1] = max(dp[k - 1][1][1], dp[k - 1][0][0] - prices[k - 1])
        return dp[m][2][0]


'''
动规空间优化：
dp[k][2][0]只与上层dp[k - 1][2][0]及dp[k - 1][2][1]有关...
因此可以借助四个变量来存储上层相应位置的值
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(1)

'''
class Solution(object):
    def maxProfit(self, prices):
        dpi10 = 0
        dpi11 = -float('inf')
        dpi20 = 0
        dpi21 = -float('inf')
        m = len(prices)
        for k in range(1, m + 1):
            dpi20 = max(dpi20, dpi21 + prices[k - 1])
            dpi21 = max(dpi21, dpi10 - prices[k - 1])
            dpi10 = max(dpi10, dpi11 + prices[k - 1])
            dpi11 = max(dpi11, - prices[k - 1])
        return dpi20






def maxProfit(prices):
    m = len(prices)
    dp = [[[0] * 2 for _ in range(2 + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0][1] = -float('inf')
    for j in range(3):
        dp[0][j][1] = -float('inf')

    for i in range(1, m + 1):
        for j in range(1, 2):
            dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])
            dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i - 1])
    return dp[m][2][0]


def maxProfit1(prices):
    m = len(prices)
    dp = [[[0] * 2 for _ in range(2 + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0][1] = -float('inf')
    for j in range(3):
        dp[0][j][1] = -float('inf')

    for i in range(1, m + 1):
        dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i - 1])
        dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i - 1])
        dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i - 1])
        dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][0] - prices[i - 1])
    return dp[m][2][0]


def maxProfit2(prices):
    m = len(prices)
    dp10 = 0
    dp11 = -float('inf')
    dp20 = 0
    dp21 = -float('inf')

    for i in range(m):
        dp10 = max(dp10, dp11 + prices[i])
        dp11 = max(dp11, -prices[i])
        dp20 = max(dp20, dp21 + prices[i])
        dp21 = max(dp21, dp10 - prices[i])
    return dp20








