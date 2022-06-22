'''
#############################################################################################################
前序遍历
#############################################################################################################
'''
'''
递归方法：
根左右，处理左右时有可使用同样的遍历方法，因此可用递归实现
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def __init__(self):
        self.res = []
    def preorderTraversal(self, root):
        if not root:
            return []
        self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.res
'''
迭代方法：
将最左侧节点压入栈中，因为是前序遍历，也需要将左侧结点加入最终结果中，当左侧结点不存在时，开始遍历当前结点的
右侧结点
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def preorderTraversal(self, root):
        res = []
        if not root:
            return res
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            root = stack.pop()
            root = root.right
        return res


'''
#############################################################################################################
中序遍历
#############################################################################################################
'''

'''
递归方法：
左根右，处理左右子树的时候可以使用同样的遍历方法
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root):
        if not root:
            return []
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)
        return self.res
'''
迭代方法：
将左侧结点全部压入栈中，当左侧节点不存在时，从栈中取值，加入最终结果中，继续处理该节点的右结点
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def inorderTraversal(self, root):
        stack, res = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

'''
#############################################################################################################
后序遍历
#############################################################################################################
'''

'''
递归方法：
左右根，处理左右子树的时候可以使用同样的遍历方法
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def __init__(self):
        self.res = []
    def postorderTraversal(self, root):
        if not root:
            return []
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.res.append(root.val)
        return self.res

'''
迭代方法：
将左侧结点全部压入栈中，当左侧节点不存在时，从栈中取值，如果该值不存在右结点或者该值的右结点刚刚有遍历过，
则将该值放入最终结果；如果该值存在右结点，因为是执行左右根，说明该值不应该出栈，继续遍历该值的右结点
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def postorderTraversal(self, root):
        stack, res, prev = [], [], None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev, root = root, None
            else:
                stack.append(root)
                root = root.right
        return res

'''
#############################################################################################################
层次遍历
#############################################################################################################
'''

'''
迭代方法：
层次遍历通过队列实现，每次取出队列首部的元素，对该元素执行左右遍历
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        queue, res = [root], []
        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                tmp.append(node.val)
            res.append(tmp)
        return res

'''
递归方法：
不需要创建临时列表存储每层的值，而是通过level来记录每个值该存放的层次
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(树高h)
'''
class Solution(object):
    def __init__(self):
        self.res = []
    def levelOrder(self, root):
        if not root:
            return []
        self.dfs(1, root)
        return self.res
    def dfs(self, level, root):
        if len(self.res) < level:
            self.res.append([])
        self.res[level - 1].append(root.val)
        if root.left:
            self.dfs(level + 1, root.left)
        if root.right:
            self.dfs(level + 1, root.right)

'''
#############################################################################################################
锯齿形层序遍历
#############################################################################################################
'''
'''
对level进行判断，从而确定值应该顺序放置还是逆序放置
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        queue, res, level = [root], [], 1
        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                tmp.append(node.val)
            if level % 2 != 0:
                res.append(tmp[:])
            else:
                res.append(tmp[::-1])
            level += 1
        return res

'''
递归方法：
对level进行判断，从而确定值应该顺序放置还是逆序放置
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(树高h)
'''
import collections
class Solution(object):
    def __init__(self):
        self.res = []
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        self.dfs(1, root)
        return [list(q) for q in self.res]
    def dfs(self, level, root):
        if len(self.res) < level:
            self.res.append(collections.deque())
        if level%2 != 0:
            self.res[level - 1].append(root.val)
        else:
            self.res[level - 1].appendleft(root.val)
        if root.left:
            self.dfs(level + 1, root.left)
        if root.right:
            self.dfs(level + 1, root.right)