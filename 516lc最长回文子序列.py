'''
#############################################################################################################
**题目516：（数组）
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
**示例：
输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。
**条件：
1 <= s.length <= 1000
s 仅由小写英文字母组成
#############################################################################################################
'''
'''
动规方法：
dp定义：dp[i][j]表示s[i]到s[j]的最长回文子序列的长度
状态转移方程：
            s[i]=s[j]:最长回文子序列的长度由内层dp[i+1][j-1]的最大回文子序列的长度+新增的i与j
            s[i]!=s[j]:最长回文一定不会同时包含i与j，因此由dp[i+1][j]与dp[i][j-1]来决定，
            以上决定了dp的值要从下至上。从左至右求解
base case：主对角线全为1，对角线下方全为0,对角线上方待求解
复杂度分析：
时间复杂度：O(N^2)
空间复杂度：O(N^2)
'''
class Solution(object):
    def longestPalindromeSubseq(self, s):
        m = len(s)
        dp=[[0] * m for _ in range(m)]
        for i in range(m):
            dp[i][i] = 1
        for i in range(m-1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][m - 1]

'''
动规优化：
左下角与下方元素均是本层求解的上层元素，因此可以将二维dp优化为一维dp，但由于dp是从左到右计算的，计算当前层
的dp[j]之后会覆盖掉上层的dp[j]，在求解dp[j+1]时左下角的值已不是上层的值，因此需要变量来保存覆盖之前的值。
复杂度分析：
时间复杂度：O(N^2)
空间复杂度：O(N)
'''
class Solution(object):
    def longestPalindromeSubseq(self, s):
        m = len(s)
        dp=[1] * m
        for i in range(m - 1, -1, -1):
            dp_left_low = 0
            for j in range(i + 1, m):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = dp_left_low + 2
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                dp_left_low = tmp
        return dp[-1]













def longestPalindromeSubseq(s):
    m = len(s)
    dp = [[0] * m for _ in range(m)]
    for i in range(m):
        dp[i][i] = 1
    for i in range(m - 1, -1, -1):
        for j in range(i + 1, m):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1], dp[i + 1][j - 1])
    return dp[0][m - 1]



def longestPalindromeSubseq1(s):
    m = len(s)
    dp = [1] * m
    for i in range(m - 1, -1, -1):
        left_low = 0
        for j in range(i + 1, m):
            tmp = dp[j]
            if s[i] == s[j]:
                dp[j] = left_low + 2
            else:
                dp[j] = max(dp[j - 1], dp[j])
            left_low = tmp
    return dp[-1]








