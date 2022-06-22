'''
#############################################################################################################
**题目62：（数组）
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
**示例：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
**条件：
1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109
#############################################################################################################
'''

'''
动规方法：
dp定义：dp[i][j]表示从start位置到i行j列
状态转移方程：
            机器人每次只能向下或者向右移动一步，决定了dp[i][j]的值有左边dp[i][j-1]及上边dp[i-1][j]来决定
            因此有dp[i][j]=dp[i-1][j]+dp[i][j-1]
base case: 第一行及第一列的值全部为1，除此之外的值待求解
复杂度分析：
时间复杂度：O(M*N)
空间复杂度：O(M*N)
'''

class Solution1(object):
    def uniquePaths(self, m, n):
        dp=[[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]

'''
动规优化：
dp[i][j]只与dp[i-1][j]及dp[i][j-1]有关，也就是只与上层的当前位置值及刚刚求解的前面位置的值有关
复杂度分析：
时间复杂度：O(M*N)
空间复杂度：O(N)
'''

class Solution1(object):
    def uniquePaths(self, m, n):
        dp=[1]*n
        for i in range(1,m):
            for j in range(1,n):
                dp[j]=dp[j]+dp[j-1]
        return dp[-1]









def uniquePaths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]



def uniquePaths1(m, n):
    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j - 1]
    return dp[-1]








