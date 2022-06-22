'''
#############################################################################################################
**题目132：（数组）
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
返回符合要求的 最少分割次数
**示例：
输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
**说明：
1 <= s.length <= 2000
s 仅由小写英文字母组成
#############################################################################################################
'''

'''
动规方法+dfs：
动规方法存储回文子串的情况；在不断寻找最小路径的过程中判断最小的子串
时间复杂度：O(M*2^M)
空间复杂度：O(M^2)
'''
class Solution(object):
    def __init__(self):
        self.nums1 = float('inf')
    def minCut(self, s):
        m = len(s)
        dp = [[True] * m for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(i + 1, m):
                if s[i] == s[j] and (j - i == 1 or dp[i + 1][j -1]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False

        self.dfs(0, [], m, dp, s)
        return self.nums1
    def dfs(self, start, tmp, m, dp, s):
        if start == m:
            self.nums1 = min(self.nums1, len(tmp) - 1)
            return
        for i in range(start, m):
            if dp[start][i]:
                tmp.append(s[start:i + 1])
                self.dfs(i+1, tmp, m, dp, s)
                tmp.pop(-1)

'''
动规方法：
动规方法存储回文串的情况，动规方法来寻找最小划分次数
dp1定义：dp1[i]表示从0到i位置的最小分割次数
状态转移方程：dp1[i]是由i位置之前的最小划分次数的位置j加上j+1~i的1次划分，前提是j+1~i是回文子串
            特殊情况：当0~i本身就是回文子串时，dp1[i]=0
base case:开始位置0时的划分次数为0
时间复杂度：O(M^2)
空间复杂度：O(M^2)
'''
def minCut1( s):
    m = len(s)
    dp = [[True] * m for _ in range(m)]

    for i in range(m - 1, -1, -1):
        for j in range(i + 1, m):
            if s[i] == s[j] and (j - i == 1 or dp[i + 1][j - 1]):
                dp[i][j] = True
            else:
                dp[i][j] = False

    dp1 = [m] * m ##求解最小值，可以放置一个不会出现的大值
    # dp1[0] = 0
    for i in range(m):
        if dp[0][i]:
            dp1[i] = 0
        for j in range(i):
            if dp[j + 1][i]:
                dp1[i] = min(dp1[i], dp1[j]+1)
    return dp1[-1]























def minCut(s):
    m = len(s)
    dp = [[False] * m for _ in range(m)]
    for i in range(m - 1, -1, -1):
        for j in range(i, m):
            if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True

    dp1 = [m] * m
    for i in range(m):
        if dp[0][i]:
            dp1[i] = 0
        for j in range(i):
            if dp[j + 1][i]:
                dp1[i] = min(dp1[i], dp1[j] + 1)
    return dp1[-1]



















def minCut7(s):
    m = len(s)
    dp = [[False] * m for _ in range(m)]

    for i in range(m - 1, -1, -1):
        for j in range(i, m):
            if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True

    dp1 = [m] * m
    for i in range(m):
        if dp[0][i]:
            dp1[i] = 0
            continue
        for j in range(i):
            if dp[j + 1][i]:
                dp1[i] = min(dp1[i], dp1[j] + 1)
    return dp[-1]
























