'''
#############################################################################################################
**题目120：（链表）
给定一个三角形 triangle ，找出自顶向下的最小路径和。
每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
**示例：
输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
**条件：
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
#############################################################################################################
'''


'''
dp定义：dp[i][j]表示从开始到第i行第j列的最小路径值
状态转移方程：由于原始矩阵是三角形结构，因此在计算时需要考虑边界问题
当j位于左边界时，最小值仅由上层同位置的值来决定；
当j位于右边界时，最小值由上层左侧值来决定；
当j位于边界中间时，最小值由同上层同位置及左侧值来决定
base case：triangle[0][0]为其本身
复杂度分析：
时间复杂度：O(M*N)  N是变化的
空间复杂度：O(M*N)
'''
class Solution(object):
    def minimumTotal(self, triangle):
        dp=triangle
        m=len(triangle)
        for i in range(1,m):
            n=len(triangle[i])
            for j in range(n):
                if 0<j<n-1:
                    dp[i][j]=min(dp[i-1][j]+triangle[i][j],dp[i-1][j-1]+triangle[i][j])
                elif j==0:
                    dp[i][j]=dp[i-1][j]+triangle[i][j]
                elif j==n-1:
                    dp[i][j] =dp[i-1][j-1]+triangle[i][j]
        return min(dp[-1])


'''
空间优化：
dp[i][j]的计算过程与triangle无关，因此可以在原triangle上修改
复杂度分析：
时间复杂度：O(M*N)
空间复杂度：O(1)
'''
class Solution(object):
    def minimumTotal(self, triangle):
        m=len(triangle)
        for i in range(1,m):
            n=len(triangle[i])
            for j in range(n):
                if 0<j<n-1:
                    triangle[i][j]=min(triangle[i-1][j]+triangle[i][j],triangle[i-1][j-1]+triangle[i][j])
                elif j==0:
                    triangle[i][j]=triangle[i-1][j]+triangle[i][j]
                elif j==n-1:
                    triangle[i][j] =triangle[i-1][j-1]+triangle[i][j]
        return min(triangle[-1])


'''
由于三角形上窄下宽，在计算的时候由底层向上层计算，就无需考虑越界的问题
dp定义：dp[i][j]表示从i行j列的位置到最后一行的最小路径值
状态转移方程：dp[i][j]由下层同位置dp[i+1][j]及右侧位置dp[i+1][j+1]来决定
base case:最后一行为其本身的值
复杂度分析：
时间复杂度：O(M*N) N在变化
空间复杂度：O(1)
'''
class Solution(object):
    def minimumTotal(self, triangle):
        m=len(triangle)
        if m==0:
            return 0
        if m==1:
            return min(triangle[0])
        for i in range(m-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j]=min(triangle[i][j]+triangle[i+1][j],triangle[i][j]+triangle[i+1][j+1])
        return triangle[0][0]






def minimumTotal(triangle):
    m = len(triangle)
    for i in range(1, m):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
            else:
                triangle[i][j] = min(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]
    return min(triangle[m - 1][:])





















