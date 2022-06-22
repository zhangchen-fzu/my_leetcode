'''
#############################################################################################################
**题目90：（回溯）
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
**示例：
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
**条件：
1 <= nums.length <= 10
-10 <= nums[i] <= 10
#############################################################################################################
'''
'''
暴力方法：
与78子集方法一样，不同点是在加入res时需要先搜索一下tmp是否在res中
复杂度分析：
时间复杂度：O(N*2^N)
空间复杂度：O(N)
'''
class Solution(object):
    def __init__(self):
        self.res = []
    def subsetsWithDup(self, nums):
        nums.sort()
        self.backtrack(nums, 0, [])
        return self.res
    def backtrack(self, nums, start, tmp):
        if tmp not in self.res:
            self.res.append(tmp[:])
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            self.backtrack(nums, i + 1, tmp)
            tmp.pop()
'''
剪枝方法：
对于当前位置来说，相同的值只能放入一次，可通过与i-1位置的值比较来剪枝
复杂度分析：
时间复杂度：O(N*2^N)
空间复杂度：O(N)
'''
class Solution1(object):
    def __init__(self):
        self.res = []
    def subsetsWithDup(self, nums):
        nums.sort()
        self.backtrack(nums, 0, [])
        return self.res
    def backtrack(self, nums, start, tmp):
        self.res.append(tmp[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            tmp.append(nums[i])
            self.backtrack(nums, i + 1, tmp)
            tmp.pop()