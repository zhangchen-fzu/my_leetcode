'''
#############################################################################################################
**题目113：（二叉树）
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
叶子节点 是指没有子节点的节点。
**示例：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]
**条件：
树中节点总数在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
#############################################################################################################
'''
class Solution(object):
    def __init__(self):
        self.res=[]
    def pathSum(self, root, targetSum):
        self.path_find(root, targetSum, [])
        return self.res
    def path_find(self,root, targetSum, tmp):
        if not root:
            return
        tmp.append(root.val)
        if not root.left and not root.right:
            if targetSum == root.val:
                self.res.append(tmp[:])
        self.path_find(root.left,targetSum - root.val, tmp)
        self.path_find(root.right, targetSum - root.val, tmp)
        tmp.pop()