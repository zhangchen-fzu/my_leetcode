'''
暴力方法: (05回文子串)
枚举+回文判断
复杂度分析：
时间复杂度：O(N^2logN)
空间复杂度：O(1)
'''
class Solution3(object):
    def longestPalindrome(self, s):
        m = len(s)
        max_str, max_len = '', 0
        for i in range(m):
            for j in range(i + 1, m + 1): ##左闭右开
                sub_str = s[i:j]
                sub_str_len=len(sub_str)
                if self.judgePalindrome(sub_str) and max_len<sub_str_len:
                    max_len=sub_str_len
                    max_str=sub_str
        return max_str
    def judgePalindrome(self, sub_str):
        l, r = 0, len(sub_str)-1
        while l < r:
            if sub_str[l] == sub_str[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

'''
#############################################################################################################
**题目300：（数组）
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
**示例：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
**条件：
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
**进阶：
你可以设计时间复杂度为 O(n2) 的解决方案吗？
你能将算法的时间复杂度降低到 O(n log(n)) 吗?
#############################################################################################################
'''

'''
动规方法：
dp定义：dp[i]表示以nums[i]为结尾的最长递增子序列的长度
状态转移方程：在i的右侧，找一个比nums[i]小的值，在该值对应的序列中加入nums[i]可组成递增子序列，对nums[i]左侧所有的比
nums[i]小的值中，找到dp值最大的+1，即为以nums[i]为结尾的最长递增子序列的长度
base case:每个值都是长度为1的递增子序列
复杂度分析：
时间复杂度：O(N^2)
空间复杂度：O(N)
'''
class Solution1(object):
    def lengthOfLIS(self, nums):
        m = len(nums)
        dp = [1] * m
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

'''
耐心排序：（二分）
放牌规则：把点数小的牌压到点数比它大的牌上；如果当前牌点数较大没有可放置的堆，则新建一个堆，
把这张牌放进去；如果当前牌有多个堆可供选择，则选择最左边的那一堆放置，因为要凑出递增序列。（二分寻找左边界）
复杂度分析：
时间复杂度：O(NlogN)
空间复杂度：O(N)
'''
class Solution2(object):
    def lengthOfLIS(self, nums):
        m = len(nums)
        top_poker = [0] * m
        plies = 0
        for i in range(m):
            poker = nums[i]

            left = 0
            right = plies
            while left < right:
                mid = (left + right) // 2
                if top_poker[mid] >= poker:
                    right = mid
                else:
                    left = mid + 1

            if left == plies:
                plies += 1
            top_poker[left] = poker
        return plies
























def lengthOfLIS(nums):
    m = len(nums)
    dp = [1] * m
    for i in range(1, m):
        for j in range(i - 1, -1, -1):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def lengthOfLIS1(nums):
    m = len(nums)
    top_poker = [0] * m
    piles = 0
    for i in range(m):
        poker = nums[i]
        left = 0
        right = piles
        while left < right:
            mid = (left + right) // 2
            if top_poker[mid] >= poker:
                right = mid
            else:
                left = mid + 1
        if left == piles:
            piles += 1
        top_poker[left] = poker
    return piles














