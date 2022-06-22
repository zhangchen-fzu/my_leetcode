'''
#############################################################################################################
**题目309：（数组）
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
**示例：
输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
**条件：
1 <= prices.length <= 105
0 <= prices[i] <= 105
#############################################################################################################
'''

'''
动规方法：
k还是处于无限次的状态，与122题一样，不同之处在于，这道题在卖出后需隔一天再买入股票，因此有
dp[i][1] = max(dp[i-1][1], dp[i-2][0]- prices[i-1])
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def maxProfit(self, prices):
        dp=[[0] * 2 for _ in range(len(prices) + 1)]
        dp[0][1] = -float('inf')
        for i in range(1,len(prices) + 1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
            if i==1:
                dp[i][1] = max(dp[i-1][1], - prices[i-1])
            else:
                dp[i][1] = max(dp[i-1][1], dp[i-2][0]- prices[i-1])
        return dp[len(prices)][0]
'''
动规优化：
dp[i-2][0]特殊，需要用独立变量dppre来存储
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(1)
'''
class Solution(object):
    def maxProfit(self, prices):
        dpi0=0
        dpi1=-float('INF')
        dppre=0
        for i in range(len(prices)):
            temp=dpi0
            dpi0=max(dpi0,dpi1+prices[i])
            dpi1=max(dpi1,dppre-prices[i])
            dppre=temp
        return dpi0












def maxProfit(prices):
    m = len(prices)
    dp = [[0] * 2 for _ in range(m + 1)]
    dp[0][1] = -float('inf')

    for i in range(1, m + 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
        if i == 1:
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i - 1])
        elif i > 1:
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i - 1])
    return dp[m][0]




def maxProfit1(prices):
    m = len(prices)
    dp0 = 0
    dp1 = -float('inf')
    top_top_val = 0

    for i in range(m):
        tmp = dp0
        if i == 0:
            dp0, dp1 = max(dp0, dp1 + prices[i]), max(dp1, dp0 - prices[i])
        else:
            dp0, dp1 = max(dp0, dp1 + prices[i]), max(dp1, top_top_val - prices[i])
        top_top_val = tmp
    return dp0







