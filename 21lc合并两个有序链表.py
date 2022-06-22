'''
#############################################################################################################
**题目21：（链表）
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
**示例：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
#############################################################################################################
'''

'''
迭代方法：
l1所指结点与l2所指结点比较，将小的节点接在新的链表上，移动小值所在的节点及新链表的节点
复杂度分析：
时间复杂度：O(M+N)
空间复杂度：O(1)
'''
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        new_head1 = ListNode(0)
        new_head = new_head1
        while l1 and l2:
            if l1.val < l2.val:
                new_head.next = l1
                l1 = l1.next
            else:
                new_head.next = l2
                l2 = l2.next
            new_head = new_head.next
            new_head.next = None
        new_head.next = l1 if l1 != None else l2
        return new_head1.next

'''
递归方法：
判断l1对应值与l2对应值的大小，小值的next通过递归继续比较及链接
复杂度分析：
时间复杂度：O(M+N)
空间复杂度：O(M+N)
'''
def mergeTwoLists(l1, l2):
    if l1 == None or l2 == None:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2