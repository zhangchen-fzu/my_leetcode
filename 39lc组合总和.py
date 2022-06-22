'''
#############################################################################################################
**题目39：（回溯）
给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。
candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 
对于给定的输入，保证和为 target 的唯一组合数少于 150 个。
**示例：
输入: candidates = [2,3,6,7], target = 7
输出: [[7],[2,2,3]]
**条件：
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500
#############################################################################################################
'''
'''
回溯方法：
与77不同的是，下次的迭代还是会从当前位置开始，因为允许一个值重复出现
复杂度分析：
试驾复杂度：O(S)，其中S为所有可行解的长度之和
空间复杂度：O(target)
'''

class Solution(object):
    def __init__(self):
        self.res = []
    def combinationSum(self, candidates, target):
        self.sub_comb(0, candidates, target, [])
        return self.res
    def sub_comb(self, start, candidates, target, tmp):
        if target == 0:
            self.res.append(tmp[:])
        if target < 0:
            return
        for i in range(start, len(candidates)):
            tmp.append(candidates[i])
            self.sub_comb(i, candidates, target - candidates[i], tmp)
            tmp.pop()

