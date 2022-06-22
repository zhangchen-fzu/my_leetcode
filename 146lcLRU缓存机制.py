'''
#############################################################################################################
**题目146：（设计）
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：
LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，
则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
**示例：
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]
解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
**条件：
1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 105 次 get 和 put
**进阶：
进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
#############################################################################################################
'''

'''
为了插入、删除方便使用双向链表结构，为了查找方便使用字典结构
get操作：元素不在，直接返回-1；元素在，拿到对应的值，并将该节点提到最前，使用方法：删除，重新加入该节点
put操作：元素在，将该节点删除，再重新加入，重新在字典中为其赋值；元素不在，若缓存容量达到上限，则将最后的元素删除，在字典中删除，将新值加入最前，在字典中加入；
若缓存容量未达到上限，则直接将该元素加入最前，在字典中加入
remove操作：改变指针
add_first操作：改变指针
'''
class ListNode(object):
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        self.max_capacity = capacity
        self.key_val_dic = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head


    def add_first(self, node): ##节点
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head


    def remove(self, node): ##节点
        node.prev.next = node.next
        node.next.prev = node.prev


    def get(self, key): ##值
        if key not in self.key_val_dic:
            return -1
        value = self.key_val_dic[key].val
        self.put(key, value)
        return value

    def put(self, key, value): ##值，值
        node = ListNode(key, value)
        if key in self.key_val_dic:
            self.remove(self.key_val_dic[key])
            self.add_first(node)
            self.key_val_dic[key] = node
        else:
            if len(self.key_val_dic) == self.max_capacity:
                end_node = self.tail.prev
                self.remove(end_node)
                del self.key_val_dic[end_node.key]
            self.add_first(node)
            self.key_val_dic[key] = node
