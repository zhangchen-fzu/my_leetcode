'''
#############################################################################################################
**题目11：（数组）
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
**示例：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
**条件：
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
#############################################################################################################
'''
'''
twosum方法：
循环nums中的每个数，计算与目标值0的差距，在其后面通过twosum（双指针）找合适的值
复杂度分析：
时间复杂度：O(N^2)
空间复杂度：O(1)

'''

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: ##剪枝1
                continue
            target=0-nums[i]

            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:  ##剪枝2
                    l += 1
                elif nums[l] + nums[r] > target:  ##剪枝2
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    while l < r and nums[r - 1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
        return result
