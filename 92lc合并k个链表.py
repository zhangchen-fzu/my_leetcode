'''
#############################################################################################################
**题目92：（链表）
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
**示例：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
#############################################################################################################
'''

'''
暴力方法：
两两合并，新合并好的结果再与下一个链表合并
复杂度分析：
时间复杂度：O(M^2*N) 其中M为链表的个数，N为链表的最长长度
空间复杂度：O(1)
'''
class Solution1(object):
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        res = lists[0]
        for i in range(1, len(lists)): #n
            res = self.merge_two_list(res, lists[i])
        return res
    def merge_two_list(self, lst1, lst2):
        if lst1 == None or lst2 == None:
            return lst1 or lst2
        if lst1.val < lst2.val:
            lst1.next = self.merge_two_list(lst1.next, lst2)
            return lst1
        else:
            lst2.next = self.merge_two_list(lst1, lst2.next)
            return lst2

'''
暴力方法的改进1（递归）：
类似于归并排序，先不断去分解，直到分解为单一链表为止，然后去合并两个链表
复杂度分析：
时间复杂度：O(MNlogM)
空间复杂度：O(logM)
'''
class Solution3(object):
    def mergeKLists(self, lists):
        m = len(lists)
        if m == 0:
            return None
        return self.merge(lists, 0, m - 1)

    def merge(self, lists, left, right): ##分解
        if left == right:
            return lists[left]
        mid = (right + left) // 2
        lst1 = self.merge(lists, left, mid)
        lst2 = self.merge(lists, mid + 1, right)
        return self.merge2list(lst1, lst2)

    def merge2list(self, lst1, lst2):  ##合并
        if lst1 == None or lst2 == None:
            return lst1 or lst2
        if lst1.val < lst2.val:
            lst1.next = self.merge2list(lst1.next, lst2)
            return lst1
        else:
            lst2.next = self.merge2list(lst1, lst2.next)
            return lst2


'''
小堆：
根据链表的节点值构建小堆，每次拿出堆顶元素（当前最小），将堆顶元素所在链表的下一个节点加入到堆中
对堆的操作：删除节点pop（获取堆顶元素，用堆中最后一个元素去替换堆顶元素，再将堆顶元素下沉到合适的位置）；
增加节点push（添加到堆的末尾，在将该元素上浮到合适的位置）
复杂度分析：
时间复杂度：O(MNlogM)
空间复杂度：O(M) 
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution4(object):
    def __init__(self):
        self.queue = []
        self.size = 0
    def mergeKLists(self, lists):
        for lst in lists:
            if lst:
                self.push(lst)
        new_node = ListNode(0)
        new_node1 = new_node
        while self.size > 0:
            node = self.pop()
            new_node1.next = node
            if node.next:
                self.push(node.next)
            new_node1 = new_node1.next
        return new_node.next

    def push(self,lst):  ##构建
        self.queue.append(lst)
        self.size += 1
        indx = self.size - 1
        while indx > 0:
            parent = (indx - 1) // 2
            if self.queue[parent].val > self.queue[indx].val:
                self.swap(parent, indx)
            else:
                break
            indx = parent

    def pop(self):  ##删除
        top = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop(-1)
        self.size -= 1
        indx = 0
        while self.size > indx:
            left = indx * 2 + 1
            right = indx * 2 + 2
            small_indx = indx
            if left < self.size and self.queue[left].val < self.queue[indx].val:
                small_indx=left
            if right < self.size and self.queue[right].val < self.queue[small_indx].val:
                small_indx = right
            if small_indx == indx:
                break
            self.swap(small_indx, indx)
            indx = small_indx
        return top

    def swap(self,parent,indx): ##交换
        self.queue[parent], self.queue[indx] = self.queue[indx], self.queue[parent]