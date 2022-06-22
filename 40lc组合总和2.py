'''
#############################################################################################################
**题目40：（回溯）
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
注意：解集不能包含重复的组合。 
**示例：
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
**条件：
输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
#############################################################################################################
'''
'''
回溯方法：
由于包含重复元素，所以需要先排序，在循环体内需要剪枝操作，其他的与39一样
复杂度分析：
时间复杂度：O(N*2^N)
空间复杂度：O(N)
'''
class Solution(object):
    def __init__(self):
        self.res = []
    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.sub_comb(0, candidates, target, [])
        return self.res
    def sub_comb(self, start, candidates, target, tmp):
        if target == 0:
            self.res.append(tmp[:])
        if target < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            tmp.append(candidates[i])
            self.sub_comb(i + 1, candidates, target-candidates[i], tmp)
            tmp.pop()