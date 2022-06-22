'''
#############################################################################################################
**题目226：（二叉树）
翻转一棵二叉树
#############################################################################################################
'''
'''
递归方法：
当前结点需要做的是交换左右子树，其他结点需要做的事交给递归
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def invertTree(self, root):
        if not root or (not root.left and not root.right):
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root