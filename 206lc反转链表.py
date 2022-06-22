'''
#############################################################################################################
**题目206：（链表）
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
**示例：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
**条件：
链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000
#############################################################################################################
'''

'''
迭代（三指针）：
pre指针控制反转之后指向的结点；cur指针控制当前结点；nxt指针存储当前结点的下一结点，是为了防止反转后找不到下一结点而去记录的结点
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(1)
'''
class Solution(object):
    def reverseList(self, head):
        pre, cur= None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
'''
递归方法：
走到链表的最后一个结点并记录下来，对当前结点head执行head.next.next来达到反转指针的效果，
注意执行一个反转之后，让head.next=None，否则会出现环
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution1(object):
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head