'''
#############################################################################################################
**题目714：（数组）
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
**示例：
输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
输出：8
解释：能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8
**条件：
1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104
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
class Solution(object):
    def maxProfit(self, prices, fee):
        dp=[[0] * 2 for _ in range(len(prices) + 1)]
        dp[0][1] = -float('inf')
        for i in range(len(prices)):
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + prices[i])
            dp[i + 1][1] = max(dp[i][1], dp[i][0] - prices[i] - fee)
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
    def maxProfit(self, prices, fee):
        dp0 = 0
        dp1 = -float('inf')
        for i in range(len(prices)):
            tmp = max(dp0,dp1 + prices[i])
            dp1 = max(dp1,dp0 - prices[i] - fee)
            dp0 = tmp
        return dp0


























def maxProfit(prices, fee):
    m = len(prices)
    dp =[[0] * 2 for _ in range(m + 1)]
    dp[0][1] = -float('inf')

    for i in range(1, m + 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i - 1] - fee)

    return  dp[m][0]


def maxProfit(prices, fee):
    m = len(prices)
    dp0 = 0
    dp1 = -float('inf')

    for i in range(m):
        dp0, dp1 = max(dp0, dp1 + prices[i]), max(dp1, dp0 - prices[i] - fee)
    return dp0








