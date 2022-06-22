'''
#############################################################################################################
**题目5：（数组）
给你一个字符串 s，找到 s 中最长的回文子串
**示例：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
**条件：
1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成
#############################################################################################################
'''
'''
中心扩展法：
从中间开始逐渐向外层扩展。将s中的每个元素都分别作为回文子串的中心，去找以该元素为中心的最大回文子串。
由于回文子串可能长度为奇数可能为偶数，扩展时需要区别对待。
复杂度分析：
时间复杂度：O(N^2)，共有N个中心，每个中心最多向外扩展N个
空间复杂度：O(1)
'''

class Solution1(object):
    def longestPalindrome(self, s):
        res = ''
        for i in range(len(s)):
            s1 = self.find_str(s, i, i) ##奇数，一个中心
            s2 = self.find_str(s, i, i + 1)  ##偶数，两个中心
            res = s1 if len(s1) > len(res) else res
            res = s2 if len(s2) > len(res) else res
        return res

    def find_str(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

'''
动规方法：
dp定义：dp[i][j]表示从i~j是否是回文子串。由于需要返回子串，所以需要定义两个变量，分别存储回文子串的起始位置及长度
状态转移方程：
            dp[i][j]=true: j-i<3 and s[i]=s[j]
            dp[i][j]=false: s[i]!=s[j]
            dp[i][j]=dp[i+1][j-1]: s[i]=s[j]
base case:单个字符一定是回文子串，dp[i][i] = True
复杂度分析：
时间复杂度：O(N^2)
空间复杂度：O(N^2)
'''
class Solution2(object):
    def longestPalindrome(self, s):
        m=len(s)
        dp=[[False]*m for _ in range(m)]
        max_len,start=0,0
        for i in range(m-1,-1,-1):
            for j in range(len(s)): ##出界的不用管，反正是False
                if s[i]==s[j] and (j-i<3 or dp[i+1][j-1]):
                    dp[i][j]=True
                    if max_len<j-i+1:
                        max_len,start=j-i+1,i
        return s[start:start+max_len]

'''
动规方法优化空间：
左下角的值可以抛弃,i控制从下到上计算，j控制从右到左计算
复杂度分析：
时间复杂度：O(N^2)
空间复杂度：O(N)
'''
class Solution3(object):
    def longestPalindrome(self, s):
        m=len(s)
        dp=[False]*m
        max_len,start=0,0
        for i in range(m-1,-1,-1):
            for j in range(m-1,-1,-1):
                if s[i]==s [j] and (j-i<3 or dp[j-1]):
                    dp[j]=True
                    if max_len<j-i+1:
                        max_len,start=j-i+1,i
        return s[start:start+max_len]











def longestPalindrome(s):
    m = len(s)
    dp = [[False] * (m) for _ in range(m)]
    start_indx, str_len = 0, 0
    for i in range(m - 1, -1, -1):
        for j in range(i, m):
            if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if j - i + 1 > str_len:
                    start_indx = i
                    str_len = j - i + 1
    return s[start_indx:start_indx + str_len]
print(longestPalindrome('abbad'))



def longestPalindrome1(s):
    m = len(s)
    dp = [False] * m
    start_indx, str_len = 0, 0
    for i in range(m - 1, -1, -1):
        left_low = False
        for j in range(i, m):
            if s[i] == s[j] and (j - i < 3 or left_low):
                left_low = dp[j],
                dp[j] = True
                if j - i + 1 > str_len:
                    start_indx = i
                    str_len = j - i + 1
            else:
                left_low = dp[j]
                dp[j] = False
    return s[start_indx:start_indx + str_len]
print(longestPalindrome1('abbad'))











