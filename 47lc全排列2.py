'''
#############################################################################################################
**题目47：（回溯）
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
**示例：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
**条件：
1 <= nums.length <= 8
-10 <= nums[i] <= 10
#############################################################################################################
'''
'''
回溯方法：
由于存在重复元素，所以与全排列Ⅰ相比需要额外的剪枝策略，将重复元素放在一起即可通过索引来剪枝
因此首先对nums排序，使用回溯方法轮流将值放入列表中，在放的过程中须注意，放过的元素不能重复放置，需要used来记录放过的元素
全排列不重复实现，通过i与前一位置i-1值相同并且前一位置的值放到过列表中该位置，i位置的值就不用再放入了该位置了
复杂度分析：
时间复杂度：O(N*N!)
空间复杂度：O(N)
'''
class Solution(object):
    def __init__(self):
        self.res = []
    def permuteUnique(self, nums):
        nums.sort()
        m = len(nums)
        used = [False] * m
        self.backtrack(nums, used, m, [])
        return self.res
    def backtrack(self, nums, used, m, tmp):
        if len(tmp) == m:
            self.res.append(tmp[:])
        for i in range(m):
            if not used[i]:
                if i>0 and nums[i]==nums[i-1] and used[i-1] == False:  ##剪枝
                    continue
                tmp.append(nums[i])
                used[i] = True
                self.backtrack(nums, used, m, tmp)
                tmp.pop()
                used[i] = False