'''
#############################################################################################################
**题目236：（二叉树）
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x
的深度尽可能大（一个节点也可以是它自己的祖先）。”
**示例：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
**条件：
树中节点数目在范围 [2, 105] 内。
-109 <= Node.val <= 109
所有 Node.val 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。
#############################################################################################################
'''
'''
递归方法：
如果p节点的父节点存在，且q节点的父节点存在，则二者的公共根节点是root，因为分布在root的左右两边；
如果p或q的父节点存在，则二者的公共根节点是存在的那个节点，
如果p和q的父节点均不存在，则二者的公共根节点也不存在
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def lowestCommonAncestor(self,  root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)  ##p与q的父节点是否有是root.left的
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


'''
字典来存储每个节点的父节点
在字典中寻找p及q的公共节点（类似于寻找链表的公共结点），找到即返回
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        node_dic = {root:None}
        def find_parent(root):
            if root:
                if root.left:
                    node_dic[root.left] = root
                if root.right:
                    node_dic[root.right] = root
                find_parent(root.left)
                find_parent(root.right)
        find_parent(root)
        l1, l2 = p, q
        while(l1 != l2):
            l1 = node_dic.get(l1, q)
            l2 = node_dic.get(l2, p)
        return l1