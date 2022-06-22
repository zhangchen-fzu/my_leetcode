'''
#############################################################################################################
**题目104：（二叉树）
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
**示例：
给定二叉树 [3,9,20,null,null,15,7]，返回它的最大深度 3
#############################################################################################################
'''


'''
bfs：
层序遍历二叉树，记录层次信息
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        queue=[root]
        level=0
        while queue:
            for i in range(len(queue)):
                node=queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return level

'''
递归：
遍历每个节点，当前节点的最大深度为：该节点左右子树的最大深度+1
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        return 1+max(left,right)
'''
0 1 1 1 1
0 0 0 1 1
1 1 0 1 1
1 1 0 0 0
1 1 1 1 0
'''
a=[[0, 1, 1, 1, 1],[0, 0, 0, 1, 1],[1, 1, 0, 1, 1],[1, 1, 0, 0, 0],[1, 1, 1, 1, 0]]
used = [[False] * len(a) for _ in range(len(a[0]))]

def find_path(i, j,path):
    if i==len(a) and j==len(a[0]):
        return path
    path_len = float('inf')
    for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
        i1=i+x
        j1=j+y
        if 0<=i1<len(a) and 0<=j1<len(a[0]) and used[i1][j1]==False and a[i1][j1]==0:
            val = find_path(i1,j1,path)
            used[i][j]=True
            path_len=min(path_len,val)
    path += path_len
    return path
# print(find_path(0,0,1))


class Solution4(object):
    def __init__(self):
        self.a = 0

    def maxAreaOfIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        res=float('inf')
        self.dfs(grid, 0, 0)
        res = min(res, self.a)
        return res

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return
        self.a += 1
        grid[i][j] = 0
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)


import sys
num = int(sys.stdin.readline().strip())
for i in range(num):
    line = sys.stdin.readline().strip()
    a, b = line.split()
    a, b = int(a), int(b)
    if a == b:
        print(0)
    k = 1
    def sub_find(a, b, k):
        if a == b:
            return 0
        min_step = 1 + min(sub_find(a + k, b, k + 1), sub_find(a - k, b, k + 1))
        return min_step
    print(sub_find(a, b, k))
