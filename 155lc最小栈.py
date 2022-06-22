'''
#############################################################################################################
**题目155：（设计）
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
**示例：
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
输出：
[null,null,null,null,-3,null,0,-2]
解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
**条件：
pop、top 和 getMin 操作总是在 非空栈 上调用
#############################################################################################################
'''
'''
两个栈，一个正常存取值，一个盛放最小值
push操作：stack正常入栈，min_stack每次入栈时比较当前值与栈顶值的大小，当其小于栈顶元素时，将该值入栈；当其大于栈顶元素时，将栈顶元素再次入栈
pop操作：先进后出原则
top操作：对stack操作
min操作：对min_stack操作
'''
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if self.min_stack == []:
            self.min_stack.append(val)
        else:
            if self.min_stack[-1] > val:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.stack.pop(-1)
        self.min_stack.pop(-1)

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
