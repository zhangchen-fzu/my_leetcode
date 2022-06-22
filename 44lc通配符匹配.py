'''
#############################################################################################################
**题目44：（数组）
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。
**示例：
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
**说明：
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
#############################################################################################################
'''


'''
dp定义：dp[i][j]表示s从0开始到i位置及p从0开始到j位置的匹配情况
状态转移方程：
如果s[i]与p[j]或p[j]是一个单通配符“?”相等，则继续处理下一个,s[i-1]与p[j-1]
如果p[j]是多通配符"*"，该通配符可以匹配s中的0、1、2,,,等字符
        该通配符是无用的：需检查s[i]与p[j-1]的情况
        该通配符与s中的一个字符匹配：需检查s[i-1]与p[j-1]的情况
        该通配符与s中的两个字符匹配：需检查s[i-2]与p[j-1]的情况
        该通配符与s中的k个字符匹配：需检查s[i-k]与p[j-1]的情况
        以上发生一个即可匹配，因此dp[i][j]=dp[i][j-1]||dp[i-1][j-1]||dp[i-2][j-1]||...||dp[i-k][j-1]
        又因为dp[i-1][j]=dp[i-1][j-1]||dp[i-2][j-1]||...||dp[i-k][j-1]
        所以dp[i][j]=dp[i][j-1]||dp[i-1][j]
base case:dp的第一行及第一列：（s,p）
    第一行：空字符串会与全*匹配
    第一列：除dp[0][0]外，其余值全部为False
    其他部分：待求
复杂度分析：
时间复杂度：O(M*N)
空间复杂度：O(M*N)
'''
class Solution(object):
    def isMatch(self, s, p):
        m=len(s)
        n=len(p)
        dp=[[False]*(n+1) for _ in range(m+1)]

        dp[0][0]=True
        for i in range(1,n+1):
            if p[i-1]=='*':
                dp[0][i]=dp[0][i-1]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
        return dp

def isMatch1(s, p):
    m = len(s)
    n = len(p)
    dp = [False] * (n + 1)

    dp[0] = True
    for i in range(1, n + 1):
        if p[i - 1] == '*':
            dp[i] = dp[i - 1]

    for i in range(1, m + 1):
        if i > 1:
            dp[0]=False
        dp_left_top=dp[0]
        print("1", dp)
        for j in range(1, n + 1):
            tmp = dp[j]
            if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                dp[j] = dp_left_top
            elif p[j - 1] == '*':
                dp[j] = dp[j] or dp[j - 1]
            else:
                dp[j]=False
            dp_left_top = tmp
    return dp
s="a"
p=""
# print(isMatch1(s,p))


def isMatch(s, p):
    m = len(s)
    n = len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = True
    for i in range(1, n + 1):
        if p[i - 1] == '*':
            dp[0][i] = dp[0][i - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    return dp
# print(isMatch(s,p))
def isMatch2( s, p):
    m = len(s)
    n = len(p)
    dp = [[False] * (n + 1) for _ in range(2)]

    dp[0][0] = True
    for i in range(2, n + 1, 2):
        if p[i - 1] == '*':
            dp[0][i] = dp[0][i - 2]

    for i in range(1, m + 1):
        print("1",dp)
        for j in range(1, n + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                dp[1][j] = dp[0][j - 1]
            elif p[j - 1] == '*':
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[1][j] = dp[1][j - 1] or dp[0][j] or dp[1][j - 2]
                else:
                    dp[1][j] = dp[1][j - 2]
            else:
                dp[1][j]=False
        dp[0][:] = dp[1][:]
    return dp
s="mississippi"
p="mis*is*p*."
print(isMatch2(s,p))

def isMatch3(s, p):
    m=len(s)
    n=len(p)
    dp=[[False]*(n+1) for _ in range(m+1)]

    dp[0][0]=True
    for i in range(2,n+1,2):
        if p[i-1]=='*':
            dp[0][i]=dp[0][i-2]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1]==p[j-1] or p[j-1]=='?':
                dp[i][j]=dp[i-1][j-1]
            elif p[j-1]=='*':
                if p[j-2]==s[i-1] or p[j-2]=='?':
                    dp[i][j]=dp[i][j-1] or dp[i-1][j] or dp[i][j-2]
                else:
                    dp[i][j]=dp[i][j-2]
    return dp
print(isMatch3(s,p))















'''
dp[i - 1][j] 表示ij的情况依赖于i-1与ｊ的情况，即ｉ已经数据ｊ了
dp[i][j - 1]表示ij的情况依赖于i与j-1的情况，即第j号元素与0个字符匹配
'''
def isMatch4(s, p):
    m = len(s)
    n = len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = True
    for i in range(1, n + 1):
        if p[i - 1] == '*':
            dp[0][i] = dp[0][i - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    return dp[m][n]












