'''
#############################################################################################################
**题目121：（数组）
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
**示例：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
**条件：
1 <= prices.length <= 105
0 <= prices[i] <= 104
#############################################################################################################
'''




'''
动规方法：
dp定义：dp[i][k][j]代表第i天，还剩买卖机会k次，目前持股状态为j。j可选0可选1,0代表目前是无股的状态，1代表目前是有股的状态
转移方程为：dp[i][k][0]=(dp[i-1][k][0],dp[i-1][k][1]+price[i])；
dp[i][k][1]=dp[i-1][k][1],dp[i-1][k-1][0]-price[i]
base case为：dp[i][0][0]=0,dp[i][0][1]=-float('inf') 
由于k固定为仅允许交易一次，因此三维dp可简化为二维dp
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution1(object):
    def maxProfit(self, prices):
        m=len(prices)
        dp=[[0]*2 for _ in range(m+1)]
        dp[0][1]=-float('inf')
        for i in range(m):
            dp[i+1][0]=max(dp[i][0],dp[i][1]+prices[i])
            dp[i+1][1]=max(dp[i][1],-prices[i])
        return dp[m][0]

'''
动规优化空间：
dp[i+1][0]只与dp[i][0]及dp[i][1]有关
dp[i+1][1]与dp[i][1]有关
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(1)
'''
class Solution1(object):
    def maxProfit(self, prices):
        m=len(prices)
        pre0=0
        pre1=-float('inf')
        for i in range(m):
            pre0=max(pre0,pre1+prices[i])
            pre1=max(pre1,-prices[i])
        return pre0


'''
贪心方法：
如果第i天股票的价格大于之前的买入的价格，那么就用在用之前的价格买入，并找后面价格最高时卖掉。
如果第i天股票的价格小于之前的买入的价格，则在第i天买入
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(1)
'''
class Solution2(object):
    def maxProfit(self, prices):
        max_val=0
        min_buy=float('inf')
        for i in range(len(prices)):
            if min_buy<prices[i]:
                max_val=max(max_val,prices[i]-min_buy)
            else:
                min_buy=prices[i]
        return max_val
















def maxProfit(prices):
    m = len(prices)
    dp = [[0] * 2 for _ in range(m + 1)]
    dp[0][1] = -float('inf')
    for i in range(1, m + 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
        dp[i][1] = max(dp[i - 1][1], -prices[i - 1])
    return max(dp[m][0], dp[m][1])






def maxProfit1(prices):
    m = len(prices)
    dp = [0, -float('inf')]
    for i in range(m):
        dp[0] = max(dp[0], dp[1] + prices[i])
        dp[1] = max(dp[1], -prices[i])
    return dp[0]


















