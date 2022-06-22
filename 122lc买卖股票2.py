'''
#############################################################################################################
**题目122：（数组）
给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
**示例：
输入: prices = [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
**条件：
1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
#############################################################################################################
'''
'''
动规方法：
dp[i][j][k]定义：第i天还剩j次交易机会，目前持股状态为k
状态转移方程：dp[i][j][0]=max(dp[i-1][j][0],dp[i-1][j][1]+price[i])
            dp[i][j][1]=max(dp[i-1][j][1],dp[i-1][j-1][0]-price[i])
base case:由于交易次数j不限制，因此可以想象成无穷次，在无穷上减一加一对结果无影响，状态转移方程可以去掉j维度，转换为二维dp
dp[0][0]=0,dp[0][1]=-float('inf')
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution1(object):
    def maxProfit(self, prices):
        dp=[[0] * 2 for _ in range(len(prices) + 1)]
        dp[0][1] = -float('inf')
        for i in range(len(prices)):
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + prices[i])
            dp[i + 1][1] = max(dp[i][1], dp[i][0] - prices[i])
        return dp[len(prices)][0]

'''
动规优化：
dp[i][0]只与dp[i-1][0]及dp[i-1][1]有关
dp[i][1]只与dp[i-1][1]及dp[i-1][0]有关
因此可借用两个变量来存储上层信息
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(1)
'''
class Solution(object):
    def maxProfit(self, prices):
        dp0 = 0
        dp1 = -float('inf')
        for i in range(len(prices)):
            tmp = max(dp0,dp1 + prices[i])
            dp1 = max(dp1,dp0 - prices[i])
            dp0 = tmp
        return dp0












def maxProfit(prices):
    m = len(prices)
    dp = [[0] * 2 for _ in range(m + 1)]
    dp[0][1] = -float('inf')
    for i in range(1, m + 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i - 1])
    return dp[m][0]


def maxProfit1(prices):
    m = len(prices)
    dp = [0, -float('inf')]
    for i in range(m):
        dp[0] = max(dp[0], dp[1] + prices[i])
        dp[1] = max(dp[1], dp[0] - prices[i])
    return dp[0]










