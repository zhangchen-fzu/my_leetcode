'''
#############################################################################################################
**题目72：（数组）
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
**示例：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
**条件：
0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成
#############################################################################################################
'''
'''
dp定义：dp[i][j]表示word1的0-i之间的字符串与word2的0-j之间的字符串匹配的最少移动次数
状态转移方程：一共有四种状态：不做任何动作、增加元素、删除元素、替换元素
当word1[i]与word2[j]相匹配时，针对当前位置不做任何动作，接着比较下一位置：word1[i-1]与word2[j-1]
当word1[i]与word2[j]不相匹配时，针对当前位置有三种行为可以执行，具体执行哪种，需要取最小：
增加元素：在word1中增加了一个元素，此时word1[i]匹配了，接下来执行word1[i-1]与word2[j]的情况
删除元素：在word1中删除了一个元素，此时word2[j]匹配了，接下来执行word2[j-1]与word1[i]的情况
替换元素：将word1[i]替换为word2[j]，此时word1[i]及word2[j]都匹配了，接下来执行word1[i-1]与word2[j-1]的情况
base case:任何一个字符串执行到末尾，总次数是需要加上另一个字符串剩余的字符数
复杂度分析：
时间复杂度：O(M*N)
空间复杂度：O(M*N)
'''
class Solution(object):
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1,dp[i][j - 1] + 1)
        return dp[m][n]

'''
动规优化：
dp[i][j]仅与dp[i-1][j-1]、dp[i-1][j]、dp[i][j-1]有关，因此可以仅保留上一层的值，但是左上角的值会被
覆盖，需要单独的变量来存储
复杂度分析：
时间复杂度：O(M*N)
空间复杂度：O(N)
'''
class Solution(object):
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [0] * (n + 1)

        for j in range(n + 1):
            dp[j] = j

        for i in range(1, m + 1):
            dp_left_top = dp[0]
            dp[0] = i
            for j in range(1, n + 1):
                tmp = dp[j]
                if word1[i - 1]== word2[j - 1]:
                    dp[j] = dp_left_top
                else:
                    dp[j] = min(dp_left_top + 1, dp[j] + 1, dp[j - 1] + 1)
                dp_left_top = tmp
        return dp[n]















def minDistance3(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[m][n]














