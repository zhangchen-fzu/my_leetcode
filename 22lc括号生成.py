'''
#############################################################################################################
**题目22：（回溯）
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
有效括号组合需满足：左括号必须以正确的顺序闭合。
**示例：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
**条件：
1 <= n <= 8
#############################################################################################################
'''
'''
暴力方法：
生成所有由"("及")"构成的序列，然后根据无论何位置左括号的数量一定大于等于右括号的数量来筛选合格的括号序列
复杂度分析：
时间复杂度：O(N*2^2N)
空间复杂度：O(N)
'''
class Solution(object):
    def generateParenthesis(self, n):
        res = []
        def generate(A):
            if len(A) == 2 * n:
                if valid(A):
                    res.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(tmp):
            num_left = 0
            for s in tmp:
                if s == '(':
                    num_left += 1
                else:
                    num_left -= 1
                if num_left < 0:
                    return False
            return num_left == 0
        generate([])
        return res

'''
回溯方法：
边构建括号序列，便去判断序列的合法性（根据剩余的左括号始终小于右括号的数量）
复杂度分析：
时间复杂度：O()
空间复杂度：O(N)
'''
class Solution1(object):
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n):
        self.backtrack(n, n, [])
        return self.res

    def backtrack(self, left, right, tmp):
        if left > right:
            return
        if left < 0 or right < 0:
            return
        if left == 0 and right == 0:
            self.res.append(''.join(tmp[:]))
            return

        tmp.append('(')
        self.backtrack(left - 1, right, tmp)
        tmp.pop()
        tmp.append(')')
        self.backtrack(left, right - 1, tmp)
        tmp.pop()