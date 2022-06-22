'''
#############################################################################################################
**题目112：（二叉树）
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，
这条路径上所有节点值相加等于目标和 targetSum 。叶子节点 是指没有子节点的节点。
**示例：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
**条件：
树中节点的数目在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
#############################################################################################################
'''
'''
递归方法：
递归的属性值有：节点，不断减小的target
停止条件：叶子结点，既无左节点又无右节点的节点
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(H) H为树的高度
'''
class Solution(object):
    def hasPathSum(self, root, targetSum):
        res = False
        if not root:
            return res
        if not root.left and not root.right:
            if root.val == targetSum:
                res = True
            return res
        res = self.hasPathSum(root.left, targetSum - root.val)
        if not res:
            res = self.hasPathSum(root.right,targetSum - root.val)
        return res

'''
代码简化
'''
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)







# import sys
# group = int(sys.stdin.readline().strip())
# for i in range(group):
#     line1 = sys.stdin.readline().strip()
#     n, k = list(map(int, line1.split()))
#     line2 = sys.stdin.readline().strip()
#     A = line2.split()
#     line3 = sys.stdin.readline().strip()
#     B = line3.split()
#     x, y, z, w = 0, 0, 0, 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if A[i] == A[j] and B[i] == B[j] and A[i] <= 'k' and B[i] <= str(k):
#                 x += 1
#             elif A[i] == A[j] and A[i] <= str(k) and B[i] != B[j]:
#                 y += 1
#             elif A[i] != A[j] and B[i] == B[j] and B[i] <= str(k):
#                 z += 1
#             else:
#                 w += 1
#     EI = (x + w) / (x + y + z + w)
#     if EI > 0.5:
#         print(1)
#     else:
#         print(0)
'''
2
5 7
1 1 2 1 1
1 3 1 2 2
5 5
1 3 2 4 1
1 1 1 1 1

'''
# import sys
# group = int(sys.stdin.readline().strip())
# for i in range(group):
#     line = sys.stdin.readline().strip()
#     n, d = list(map(int, line.split()))
#     if n < d:
#         print(0)
#     else:
#         if n**(1/2) >= d:
#             print(1)
#         else:
#             print(0)
#
# import sys
# group = int(sys.stdin.readline().strip())
# for i in range(group):
#     line1 = sys.stdin.readline().strip()
#     n, k = list(map(int, line1.split()))
#     line2 = sys.stdin.readline().strip()
#     A = line2.split()
#     line3 = sys.stdin.readline().strip()
#     B = line3.split()
#     x, y, z, w = 0, 0, 0, 0
#     count = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             count += 1
#             if A[i] == A[j] and B[i] == B[j]:
#                 x += 1
#             elif A[i] != A[j] and B[i] != B[j]:
#                 w += 1
#     EI = (x + w) / count
#     if EI > 0.5:
#         print(1)
#     else:
#         print(0)
#
#
#
#
#
# import sys
# group = int(sys.stdin.readline().strip())
# for i in range(group):
#     line1 = sys.stdin.readline().strip()
#     n, k = list(map(int, line1.split()))
#     line2 = sys.stdin.readline().strip()
#     A = line2.split()
#     line3 = sys.stdin.readline().strip()
#     B = line3.split()
#     x, y, z, w = 0, 0, 0, 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             if A[i] == A[j] and B[i] == B[j] and A[i] <= 'k' and int(B[i]) <= k:
#                 x += 1
#             elif A[i] == A[j] and int(A[i]) <= k and B[i] != B[j]:
#                 y += 1
#             elif A[i] != A[j] and B[i] == B[j] and int(B[i]) <= k:
#                 z += 1
#             elif A[i] != A[j] and B[i] != B[j]:
#                 w += 1
#     EI = (x + w) / (x + y + z + w)
#     if EI > 0.5:
#         print(1)
#     else:
#         print(0)


# import sys
# group = sys.stdin.readline().strip()
# n, k = list(map(int, group.split()))
#
# lst = sys.stdin.readline().strip()
# lst = list(map(int, lst.split()))
#
# pre_sum = [0, lst[0]]
# for j in range(1, len(lst)):
#     pre_sum.append(pre_sum[j] + lst[j])
# print(pre_sum)
#
# min_val = float('inf')
# for i in range(k, n):
#     vag = (pre_sum[i] - pre_sum[i - k]) / k
#     print(vag)
#     print(lst[:i - k],lst[k:])
#     if i == k:
#         new_lst = [vag] + lst[:i - k] + lst[k:]
#     else:
#         new_lst = [vag] + lst[:i - k] + lst[k + 1:]
#     print(new_lst)
# #     min_val = min(min_val, max(new_lst) - min(new_lst))
# # print(format(min_val,'.7f'))
# # import sys
# # # n = int(sys.stdin.readline().strip())
# # # line2 = sys.stdin.readline().strip()
# # # lst1 = list(map(int, line2.split()))
# # # count=0
# # # for i in range(len(lst1)):
# # #     for j in range(i+1, len(lst1)):
# # #         if (lst1[i] * lst1[j])**(1/2) in [ i * i for i in range(max(lst1[i]+ 1,lst1[j] + 1))]：
# # #         count+= 1
# # # print(count)
#
#
# def longestPalindrome(s):
#     m = len(s)
#     dp = [[False] * (m) for _ in range(m)]
#     start, max_len = 0, 0
#     for i in range(m - 1, -1, -1):
#         for j in range(i, m):
#             if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
#                 dp[i][j] = True
#                 if j - i + 1 > max_len:
#                     max_len = j - i + 1
#                     start = i
#     return dp
# print(longestPalindrome('a'))
#
# def longestPalindrome1(s):
#     m = len(s)
#     dp = [[False] * (m) for _ in range(m)]
#     start, max_len = 0, 0
#     for i in range(m - 1, -1, -1):
#         for j in range(i, m):
#             if i == j:
#                 dp[i][j] = True
#             else:
#                 if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
#                     dp[i][j] = True
#                     if j - i + 1 > max_len:
#                         max_len = j - i + 1
#                         start = i
#     return dp
# print(longestPalindrome1('a'))
#
# def sum(num1, num2):
#     def sub(num):
#         val1 = 0
#         tmp = 0
#         for i in range(len(num) - 1, -1, -1):
#             val1 += int(num[i]) * (8 ** tmp)
#             tmp += 1
#         return val1
#
#     a1 = sub(num1)
#     a2 = sub(num2)
#     a12 = a1 + a2
#
#     print(a12)
#     strs = []
#     while a12 != 0:
#         div, mod = divmod(a12, 8)
#         strs.append(str(mod))
#         a12 = div
#     return ''.join(strs[::-1])
# print(sum('1', '7'))

# import sys
# nums = int(sys.stdin.readline().strip())
# tmp = [1, 1, 1]
# for i in range(3, nums + 1):
#     res = tmp[-1] + tmp[0]
#     tmp = tmp[1:] + [res]
# print(tmp[-1])
# print(6 % 3)
# import sys
# # import math
# # nums = int(sys.stdin.readline().strip())
# # yu = 10 ** 9 + 7
# # gen5 = math.sqrt(5)
# # fib_nums = (math.pow((1 + gen5) / 2, nums) - math.pow((1 - gen5) / 2, nums)) % yu
# # a = int(fib_nums / (gen5 % yu))
# # print(a)
# import sys
#
# line1 = sys.stdin.readline().strip()
# n, m = list(map(int, line1.split()))
#
# graph_dic = {}
# graph = []
# for i in range(m):
#     line2 = sys.stdin.readline().strip()
#     a, b = list(map(int, line2.split()))
#     if a not in graph_dic:
#         graph_dic[a] = []
#     graph_dic[a].append(b)
#     graph.append((a, b))

# count = 0
# for j in range(len(graph)):
#     start = graph[j][0]
#     end = graph[j][1]
#     for val in graph_dic:
#         if val == end:
#             end = graph_dic[val][0]
#         if end == start:
#             count += 1
#             break
# print(count // 2)
# import sys
#
# line1 = sys.stdin.readline().strip()
# n, m = list(map(int, line1.split()))
#
# graph_dic = {}
# graph = []
# for i in range(m):
#     line2 = sys.stdin.readline().strip()
#     a, b = list(map(int, line2.split()))
#     if a not in graph_dic:
#         graph_dic[a] = []
#     graph_dic[a].append(b)
#     graph.append((a, b))
#
# count = 0
# used = [False] * len(graph)
# for j in range(len(graph)):
#     start = graph[j][0]
#     end = graph[j][1]
#     used[j] = True
#     for i, val in enumerate(graph_dic):
#         if used[i] == False and val == end:
#             end = graph_dic[val][0]
#             used[i] = True
#         if end == start:
#             count += 1
#             break
# print(count)
# import sys
# line1 = sys.stdin.readline().strip()
# n, m = list(map(int, line1.split()))
#
# graph = []
# for i in range(m):
#     line2 = sys.stdin.readline().strip()
#     a, b = list(map(int, line2.split()))
#     graph.append((a, b))
# graph.sort(key=lambda x:x[0])
#
# count = 0
# for j in range(len(graph)):
#     start = graph[j][0]
#     end = graph[j][1]
#     indx = j + 1
#     while indx < len(graph):
#         if graph[indx][0] == end:
#             end = graph[indx][1]
#         indx += 1
#     if end == start:
#         count += 1
# print(count)



















