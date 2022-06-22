'''
#############################################################################################################
**题目198：（数组）
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
**示例：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
**条件：
1 <= nums.length <= 100
0 <= nums[i] <= 400
#############################################################################################################
'''

'''
动规方法1：
dp定义：dp[i][j]表示从开始到第i家最多可抢劫的金额数，其中j为1代表抢劫第i家，j为0代表不抢劫第i家
转移方程：dp[i][0]=max(dp[i-1][1],dp[i-1][0])
        dp[i][1]=dp[i-1][0]+nums[i]
base case为：dp[0][0]=0,dp[0][1]=nums[0]
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''

class Solution1(object):
    def rob(self, nums):
        m = len(nums)
        dp = [[0] * 2 for _ in range(m)]
        dp[0][1] = nums[0]
        for i in range(1, m):
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[m - 1][1], dp[m - 1][0])

'''
动规1优化空间：
由于dp[i][0]只与dp[i-1][1]及dp[i-1][0]有关，dp[i][1]只与dp[i-1][0]有关，因此可借助两个变量存储上一层的值
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(1)
'''
class Solution1(object):
    def rob(self, nums):
        m = len(nums)
        dp0 = 0
        dp1 = nums[0]
        for i in range(1, m):
            tmp = max(dp1, dp0)
            dp1 = dp0 + nums[i]
            dp0 = tmp
        return max(dp1, dp0)

'''
动规方法2：
dp定义：dp[i]代表从第i家开始一直抢到最后一家的最大金额数
状态转移方程：dp[i]=max(dp[i+1],dp[i+2]+nums[i]),若不抢劫第i家，那就去看看第i+1家的情况；若抢劫第i家，第i+1家指定不能抢劫，那就去看看第i+2家
的情况，加上第i家抢的金额数
base case:dp[m+1]及dp[m+2]=0
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution2(object):
    def rob(self, nums):
        m = len(nums)
        dp = [0] * (m + 2)
        for i in range(m - 1, -1, -1):
            dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
        return dp[0]

'''
动规2优化空间：
dp[i]只与dp[i+1]及dp[i+2]有关，可用2个变量存储
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(1)
'''
class Solution2(object):
    def rob(self, nums):
        dpi1, dpi2, dp = 0, 0, 0
        for i in range(len(nums) - 1, -1, -1):
            dp = max(dpi1, dpi2 + nums[i])
            dpi2 = dpi1
            dpi1 = dp
        return dp


def rob(nums):
    m = len(nums)
    dp = [0, 0] + [0] * m
    for i in range(2, m + 2):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 2])
    return dp[-1]






def rob(nums):
    m = len(nums)
    dp = [0] * (m + 2)
    for i in range(m - 1, -1, -1):
        dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
    return dp[0]


def rob(nums):
    m = len(nums)
    dp1 = 0
    dp2 = 0
    for i in range(m):
        dp1, dp2 = max(dp1, dp2 + nums[i]), dp1
    return dp1








