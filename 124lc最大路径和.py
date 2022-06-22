'''
#############################################################################################################
**题目124：（二叉树）
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。
该路径 至少包含一个 节点，且不一定经过根节点。路径和 是路径中各节点值的总和。
给你一个二叉树的根节点 root ，返回其 最大路径和 。
**示例：
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
**条件：
树中节点数目范围是 [1, 3 * 104]
-1000 <= Node.val <= 1000
#############################################################################################################
'''

'''
递归方法：
以当前节点为根节点的最大路径值为，当前节点的值+左子树的最大路径值+右子树的最大路径值
子树的最大路径值=节点的值+左右子树的最大值
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def __init__(self):
        self.res = -float('inf')
    def maxPathSum(self, root):
        self.max_value(root)
        return self.res
    def max_value(self, root):
        if not root:
            return 0
        left_path_max_val = max(self.max_value(root.left), 0)
        right_path_max_val = max(self.max_value(root.right), 0)
        path_sum = root.val + left_path_max_val + right_path_max_val
        self.res = max(self.res, path_sum)
        return root.val + max(left_path_max_val, right_path_max_val)
