'''
#############################################################################################################
**题目131：（数组）
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串。
**示例：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
**说明：
1 <= s.length <= 16
s 仅由小写英文字母组成
#############################################################################################################
'''

'''
动规判断回文+DFS搜索结果：
当搜索出s[:j]是回文字符串时，接下来需要从j+1开始继续查找合适的回文，从j+1开始的回文串也许会有很多，因此需要回溯
在此过程中需要不断判断某子串是否是回文串，为节省判断的时间，可以考虑优先建立dp数组存放回文情况，以空间换时间
复杂度分析：
时间复杂度：O(M*2^M) 当字符串为同一值时，最多有2^(n-1)种划分情况，每种情况需要时间N来找出划分结果
空间复杂度：O(M^2)
'''
def partition(s):
    m = len(s)
    dp=[[True] * m for _ in range(m)]
    for i in range(m - 1, -1, -1):
        for j in range(i + 1, m):
            if s[i] == s[j] and (j - i == 1 or dp[i + 1][j - 1]):
                dp[i][j] = True
            else:
                dp[i][j] = False

    res = []
    def dfs(start, tmp):
        if start == m:
            res.append(tmp[:])
            return
        for i in range(start, m):
            if dp[start][i]:
                tmp.append(s[start:i + 1])
                dfs(i + 1, tmp)
                tmp.pop(-1)

    dfs(0, [])
    return res
















def partition1(s):
    m = len(s)
    dp = [[False] * m for _ in range(m)]
    for i in range(m - 1, -1, -1):
        for j in range(i, m):
            if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True

    res = []
    def sub(start, tmp):
        if start == m:
            res.append(tmp[:])
            return
        for k in range(start, m):
            if dp[start][k] == True:
                tmp.append(s[start:k + 1])
                sub(k + 1, tmp)
                tmp.pop()

    sub(0, [])
    return res






def partition2(s):
    m = len(s)
    dp = [[False] * m for _ in range(m)]

    for i in range(m - 1, -1, -1):
        for j in range(i, m):
            if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True

    res = []
    def sub(start, tmp):
        if start == m:
            res.append(tmp[:])
            return
        for k in range(start, m):
            if dp[start][k]:
                tmp.append(s[start:k + 1])
                sub(k + 1, tmp)
                tmp.pop()
    sub(0, [])
    return res









