'''
#############################################################################################################
**题目199：（二叉树）
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
**示例：
输入: [1,2,3,null,5,null,4]
输出: [1,3,4]
**条件：
二叉树的节点个数的范围是 [0,100]
-100 <= Node.val <= 100
#############################################################################################################
'''
'''
bfs（迭代）：
将每层的最后一个节点（最右侧）放入最终结果中
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        queue, res = [root], []
        while queue:
            last_node = None
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                last_node = node.val
            res.append(last_node)
        return res

'''
dfs（迭代）：
栈在记录节点的同时记录节点所处的深度，当该深度的值不存在时，将其加入字典中，依赖后进先出的原则刚好可以使右节点率先加入字典中，
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        res_dic = {}
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if node:
                res_dic.setdefault(depth, node.val)
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return list(res_dic.values())


'''
dfs（递归）：
根据“根右左”来遍历，同样记录深度信息，当该深度没有值时，将率先遍历的右节点加入最终结果中
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def __init__(self):
        self.res = []
    def rightSideView(self, root):
        self.dfs(root, 0)
        return self.res
    def dfs(self, root, depth):
        if not root:
            return
        if depth == len(self.res):
            self.res.append(root.val)
        self.dfs(root.right, depth + 1)
        self.dfs(root.left, depth + 1)