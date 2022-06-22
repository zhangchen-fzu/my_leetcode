'''
#############################################################################################################
**题目46：（回溯）
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
**示例：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
**条件：
1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
#############################################################################################################
'''

'''
回溯方法:
套用回溯模板。由于nums不含重复数字，所以可通过暴力匹配方法来剪枝
复杂度分析：
时间复杂度：O(N*N!)
空间复杂度：O(N)
'''

class Solution2(object):
    def __init__(self):
        self.result = []
    def permute(self, nums):
        self.backtrack(nums, [])
        return self.result
    def backtrack(self, nums, tmp):
        if len(tmp) == len(nums):
            self.result.append(tmp[:])
            return
        for i in range(len(nums)):
            if nums[i] in tmp: ##剪枝
                continue
            tmp.append(nums[i])
            self.backtrack(nums, tmp)
            tmp.pop(-1)

