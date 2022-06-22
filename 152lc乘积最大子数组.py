'''
#############################################################################################################
**题目152：（链表）
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
**示例：
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
#############################################################################################################
'''
'''
由于乘法有负负得正的现象，因此当当前值是负数时，从开始到当前位置的最大值并不是由当前位置的前一位置的最大值决定的，而是由前一位置的最小值决定的
因此计算过程中既需要保存当前的最大值又需要保存当前的最小值。
dp定义：max_value[i]表示以i位置为终点的最大值，min_value[i]表示以i为终点的最小值
状态转移方程：当前的最大值有三种可能：当前值自己、当前值*前一位置的最大值、当前值*前一位置的最小值
            当前的最小值有三种可能：当前值自己、当前值*前一位置的最大值、当前值*前一位置的最小值
base case：0位置的最大值及最小值都是其本身
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def maxProduct(self, nums):
        m = len(nums)
        max_value=[nums[0]]*m
        min_value=[nums[0]]*m
        for i in range(1,m):
            max_value[i]=max(max_value[i-1]*nums[i],min_value[i-1]*nums[i],nums[i])
            min_value[i]=min(min_value[i-1]*nums[i],max_value[i-1]*nums[i],nums[i])
        return max(max_value)

'''
空间优化：
由于max_value[i]仅与max_value[i-1]有关，min_value[i]同样，所以可使用两个变量来单独存储上一位置的值
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(1)
'''
class Solution(object):
    def maxProduct(self, nums):
        m = len(nums)
        max_value=nums[0]
        min_value=nums[0]
        res=nums[0]
        for i in range(1,m):
            max_value,min_value=max(max_value*nums[i],min_value*nums[i],nums[i]),min(min_value*nums[i],max_value*nums[i],nums[i])
            res=max(res,max_value)
        return res


def maxProduct(nums):
    m = len(nums)
    dp_min = nums[0]
    dp_max = nums[0]
    res = dp_max
    for i in range(1, m):
        dp_min,dp_max = min(nums[i], dp_min * nums[i], dp_max * nums[i]), max(nums[i], dp_min * nums[i], dp_max * nums[i])
        res = max(res, dp_max)
    return res











