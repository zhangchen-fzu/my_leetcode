'''
#############################################################################################################
**题目1143：（数组）
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
**示例：
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。
**条件：
1 <= text1.length, text2.length <= 1000
text1 和 text2 仅由小写英文字符组成。
#############################################################################################################
'''
'''
动规方法：
dp定义：dp[i][j]表示text1[0]~text1[i]与text2[0]~text2[j]的最长公共子序列的长度
状态转移方程：
            if text1[i]=text2[j]:公共子序列的长度在text1[i-1]与text2[j-1]的基础上+1
            if text1[i]！=text2[j]：公共子序列的长度一定不会是text1[i]与text2[j]同时出现，而是由text1[i]与text2[j]之一来决定
            以上决定遍历方向为：从下至上，从左至右
base case：dp[0][j]=0 and dp[i][0]=0
复杂度分析：
时间复杂度：O(N^2)
空间复杂度：O(N^2)
'''
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        dp=[[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]

'''
动规优化：
与516题相似，记录上层的信息，同时为防止左上位置的值被覆盖，用变量单独存储起来
复杂度分析：
时间复杂度：O(N^2)
空间复杂度：O(N)

'''
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        dp=[0] * (n+1)
        for i in range(1, m + 1):
            dp_left_top = 0
            for j in range(1, n + 1):
                tmp = dp[j]
                if text1[i-1] == text2[j - 1]:
                    dp[j] = dp_left_top + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                dp_left_top = tmp
        return dp[-1]







def longestCommonSubsequence(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

def longestCommonSubsequence1(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [0] * (n + 1)
    for i in range(m):
        left_top = 0
        for j in range(1, n + 1):
            tmp = dp[j]
            if text1[i] == text2[j - 1]:
                dp[j] = 1 + left_top
            else:
                dp[j] = max(dp[j], dp[j - 1])
            left_top = tmp
    return dp[-1]









