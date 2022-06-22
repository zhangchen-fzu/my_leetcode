'''
#############################################################################################################
**题目110：（二叉树）
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
**示例：
输入：root = [3,9,20,null,null,15,7]
输出：true
**条件：
树中的节点数在范围 [0, 5000] 内
-104 <= Node.val <= 104
#############################################################################################################
'''
'''
递归方法：
去计算每个节点的左右子树的深度之差是否在1之内，如果在，则返回子树的深度（左右子树的最大深度+1）；
如果不在，则返回一个永远不会取到的值-1，作为非平衡二叉树的标记
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def isBalanced(self, root):
        res = self.sub_tree_high(root)
        if res == -1:
            return False
        return True
    def sub_tree_high(self, root):
        if not root:
            return 0
        left_high = self.sub_tree_high(root.left)
        right_high = self.sub_tree_high(root.right)
        if left_high == -1 or right_high == -1 or abs(left_high-right_high) > 1:
            return -1
        elif abs(left_high - right_high) <= 1:
            return 1 + max(left_high, right_high)
