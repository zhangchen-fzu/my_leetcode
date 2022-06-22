'''
#############################################################################################################
**题目77：（回溯）
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。
**示例：
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
**条件：
1 <= n <= 20
1 <= k <= n
#############################################################################################################
'''
'''
回溯方法：
for找到每个开头的，回溯找到以该值开头的所有组合方法
复杂度分析：
时间复杂度：O(Cnk*k)
空间复杂度：O(k)
'''
class Solution(object):
    def __init__(self):
        self.res = []
    def combine(self, n, k):
        self.sub_comb(1, n, k, [])
        return self.res
    def sub_comb(self, start, n, k, tmp):
        if len(tmp) == k:
            self.res.append(tmp[:])
            return
        for i in range(start, n+1):
            tmp.append(i)
            self.sub_comb(i + 1, n, k, tmp)
            tmp.pop()

'''
优化方法：
当以某个值开始时，后面的数无法满足达到k位的要求时，直接淘汰掉这一值开头的所有组合方法
复杂度分析：
时间复杂度：O(Cnk*k)
空间复杂度：O(k)
'''
class Solution1(object):
    def __init__(self):
        self.res = []
    def combine(self, n, k):
        self.sub_comb(1, n, k, [])
        return self.res
    def sub_comb(self, start, n, k, tmp):
        if len(tmp) + (n - start + 1)< k:
            return
        if len(tmp) == k:
            self.res.append(tmp[:])
            return
        for i in range(start, n+1):
            tmp.append(i)
            self.sub_comb(i + 1, n, k, tmp)
            tmp.pop()