'''
#############################################################################################################
**题目543：（二叉树）
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
**示例：
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
注意：两结点之间的路径长度是以它们之间边的数目表示。
#############################################################################################################
'''

'''
递归方法：
当前节点需要的做是，计算以该节点为根节点的最大路径，并更新最终结果res，其他结点该做的事情交给递归
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(H)
'''
class Solution(object):
    def __init__(self):
        self.res=-float('inf')
    def diameterOfBinaryTree(self, root):
        self.max_diameter(root)
        return self.res
    def max_diameter(self,root):
        if not root:
            return 0
        left=self.max_diameter(root.left)
        right=self.max_diameter(root.right)
        self.res=max(self.res,left+right)
        return 1+max(left,right)