'''
#############################################################################################################
**题目105：（二叉树）
给定一棵树的前序遍历 preorder 与中序遍历  inorder。请构造二叉树并返回其根节点。
**示例：
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
**条件：
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder 和 inorder 均无重复元素
inorder 均出现在 preorder
preorder 保证为二叉树的前序遍历序列
inorder 保证为二叉树的中序遍历序列
#############################################################################################################
'''
'''
递归：
前序是按照根左右去遍历的，根排在前面；中序是按照左根右去遍历的，根的左侧是左子树，根的右侧是右子树
因此可以根据前序遍历去寻找根节点，根据中序遍历去寻找左右子树
复杂度分析:
时间复杂度：O(N)
空间复杂度：O(N)
'''
# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_indx = inorder.index(root_val)

        left_inorder = inorder[:root_indx]
        right_inorder = inorder[root_indx + 1:]
        m = len(left_inorder)
        root.left = self.buildTree(preorder[1:1 + m], left_inorder)
        root.right = self.buildTree(preorder[1 + m:], right_inorder)
        return root
'''
将前面的切片操作修改为记录索引
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def buildTree(self, preorder, inorder):
        val_indx_dic = {}
        m = len(inorder)
        for i in range(m):
            val_indx_dic[inorder[i]] = i
        def sub_bulid_tree(root, left, right):
            if left > right:
                return
            node_val = preorder[root]
            node_indx = val_indx_dic[node_val]
            node = TreeNode(node_val)
            node.left = sub_bulid_tree(root + 1, left,node_indx - 1)
            node.right = sub_bulid_tree(root + 1 + node_indx - left, node_indx + 1, right)
            return node
        return sub_bulid_tree(0, 0, m - 1)

