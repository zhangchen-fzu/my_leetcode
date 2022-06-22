'''
#############################################################################################################
**题目：（数组）
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
**示例：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
**条件：
1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
**进阶：
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
#############################################################################################################
'''


'''
动规方法：
dp[i]用来存放0-i的最大子序和，
如果dp[i-1]为负值时，当前值是最大子序和；否则，当前值加上前一位置的最大子序和为当前位置的最大子序和
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution1(object):
    def maxSubArray(self, nums):
        dp = nums
        for i in range(1, len(nums)):
            if dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i - 1]
        return max(dp)


'''
动规方法优化空间：
dp[i]的值只和dp[i-1]有关，因此可用bef_val来存放dp[i-1]的值
复杂度分析：
时间复杂度：O(N)
空间复杂度：0(1)
'''
class Solution1(object):
    def maxSubArray(self, nums):
        res = -float('inf')
        bef_val = -float('inf')
        for i in range(len(nums)):
            bef_val = max(nums[i], bef_val + nums[i])
            res = max(res, bef_val)
        return res







def maxSubArray(nums):
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i - 1])
    return max(nums)















