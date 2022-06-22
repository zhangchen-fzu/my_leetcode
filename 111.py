# class Stack(object):
#     def __init__(self):
#         self.stack = []
#     def pop(self):
#         self.stack.pop(-1)
#     def push(self, value):
#         self.stack.append(value)
# class Queue(object):
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#     def push(self, value):
#         self.stack1.Stack().push(value)
#     def pop(self):
#         if self.stack2 != []:
#             return self.stack2.Stack().pop()
#         else:
#             while self.stack1:
#                 self.stack2.append(self.stack1.Stack().pop())
#             return self.stack2.Stack().pop()

# import sys
# a = int(sys.stdin.readline().strip())
# lst=['1','11']
# if a == 1:
#     print(int(lst[0]))
# for i in range(2, a):
#     strs = lst[i - 1]
#     l=0
#     r=0
#     res=''
#     while r<len(strs):
#         if strs[l]==strs[r]:
#             r+=1
#         else:
#             res += str(r-l) + str(strs[l])
#             l = r
#     if r==len(strs):
#         res += str(r-l) + str(strs[l])
#     lst.append(res)
# print(lst)
# import sys
# a = int(sys.stdin.readline().strip())
# max1=-float('inf')
# max2=-float('inf')
# for i in range(a):
#     line = sys.stdin.readline().strip()
#     values = list(line)
#     # print(values)
#     max1=max(max1,abs(int(values[0])))
#     max2=max(max2,abs(int(values[2])))
# # print(max1*max2/2.0)
# import os
# import re
# import sys
# from typing import List
#
#
# class Solution:
#     def conv2d(self, kernel, image, stride):
#         k_shape = len(kernel)
#         img_shape = len(image)
#         res_size = (img_shape - k_shape) // stride + 1
#         # print(res_size)
#         res = [[0] * res_size for _ in range(res_size)]
#         row_start = 0
#         for i in range(res_size):
#             col_start = 0
#             for j in range(res_size):
#                 cut_image = image[row_start:k_shape + row_start]
#                 cut_image = [cut_image[k][col_start:col_start + k_shape] for k in range(k_shape)]
#                 # print(cut_image)
#                 res[i][j] = self.multiplyTwoMatrix(kernel, cut_image)
#                 # print(res[i][j])
#                 col_start += stride
#
#             row_start += stride
#
#         return res_size, res
#
#     def multiplyTwoMatrix(self, A: List[List[int]], B: List[List[int]]):
#         n = len(A)
#         res = 0
#         for i in range(n):
#             for j in range(n):
#                 res += A[i][j] * B[i][j]
#
#         return res


# if __name__ == "__main__":
#     kernel = input()
#     k_size, k_input = kernel.split(",")
#     k_size = int(k_size[0])
#     k_nums = list(map(int, k_input.split(" ")[1:]))
#     kernels = []
#     for i in range(0, len(k_nums), k_size):
#         kernels.append(k_nums[i:i + k_size])
#     # print(kernels)
#     # print(k_size)
#     image = input()
#     img_size, img_input = image.split(",")
#     img_size = int(img_size[0])
#     img_nums = list(map(int, img_input.split(" ")[1:]))
#     images = []
#     for i in range(0, len(img_nums), img_size):
#         images.append(img_nums[i:i + img_size])
#     # print(images)
#     stride = int(input())
#     # padding补0
#     padding_images = []
#     for _ in range(stride):
#         padding_images.append([0] * (img_size + 2 * stride))
#     for x in range(img_size):
#         padding_images.append([0] * stride + images[x] + [0] * stride)
#     for _ in range(stride):
#         padding_images.append([0] * (img_size + 2 * stride))
#     # print(padding_images)
#
#     sl = Solution()
#     # print(sl.multiplyTwoMatrix([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
#     # print(sl.conv2d(kernels, images, stride))
#     res_first, res_second = sl.conv2d(kernels, padding_images, stride)
#     ans = []
#     for a in range(res_first):
#         for b in range(res_first):
# #             ans.append(str(res_second[a][b]))
# #     print(str(res_first) + " " + str(res_first) + ", " + " ".join(ans))
# #
# # 使用的公式
# # 三角形两边之和大于第三边
# # 三角形两边之差小于第三边
#
# import math
#
#
# class Solution:
#     # return "No Answer" 33%
#     def getThirdHeight(self, x: int, y: int):
#         a, b = max(x, y), min(x, y)
#         if a == b:
#             return "No Answer"
#         # 如果a * b / (a + b)结果和a * b // (a + b)结果相同，说明数学意义上a * b / (a + b)是个整数
#         if a * b / (a + b) == a * b // (a + b):
#             # start结果加一是因为start在结果中可以取到
#             start = a * b // (a + b) + 1
#         else:
#             # 如果a * b / (a + b)结果和a * b // (a + b)结果不同，说明前者肯定大于后者，取上整数
#             start = int(math.ceil(a * b / (a + b)))
#         # 同理，end结果如果是整数，是不能取到的
#         if a * b / (a - b) == a * b // (a - b):
#             end = a * b // (a - b)
#         else:
#             # 如果不是整数，取上整
#             end = int(math.ceil(a * b / (a - b)))
#         res = []
#         # 结果中均减去1
#         for i in range(end - 1, start - 1, -1):
#             res.append(i)
#         if not res:
#             return "No Answer"
#         return res


# if __name__ == "__main__":
#     sl = Solution()
#     X, Y = input().split()
#     X, Y = int(X), int(Y)
#     print(sl.getThirdHeight(X, Y))

# import sys
# while True:
#     a=sys.stdin.readline().strip()
#     start, num = a.split()
#     start = int(start)
#     num = int(num)
#     res = 0
#     tmp = start
#     for i in range(num):
#         res += tmp
#         tmp = tmp ** (0.5)
#     print("%.2f"%res)
# import sys
# while True:
#     a = sys.stdin.readline().strip()
#     start, end = a.split()
#     start = int(start)
#     end = int(end)
#     lst = ''
#     for i in range(start, end + 1):
#         strs = str(i)
#         if int(strs[0]) ** 3 + int(strs[1]) ** 3 + int(strs[2]) ** 3 == int(strs):
#             if lst == '':
#                 lst += strs
#             else:
#                 lst += (' ' + strs)
#     if lst == '':
#         print('no')
#     else:
#         print(lst)
# import sys
# # a = sys.stdin.readline().strip()
# # a1, a2, a3 = a.split()
# # b = sys.stdin.readline().strip()
# # b1, b2, b3 = b.split()
# # c = sys.stdin.readline().strip()
# # c1, c2, c3 = c.split()
# # d = sys.stdin.readline().strip()
# # d1, d2, d3 = d.split()
# # print(0)

# import sys
# matrix = []
# while True:
#     a = sys.stdin.readline().strip()
#     matrix.append(a.split())
#
# used= [[False]*len(matrix[0]) for _ in range(len(matrix))]
# count=0
# def find_path(i, j):
#     for x, y in [(0,-1),(-1,0),(0,1),(1,0)]:
#         i1=i+x
#         j1=j+y
#         if 0<=i1<len(matrix) and 0<=j1<len(matrix[0]) and used[i1][j1]== False and matrix[i1][j1]=='1':
#             count+=1
#             used[i1][j1]=True
#     return count
# print(find_path(0, 0))

# import sys
# num = sys.stdin.readline().strip()
# m = len(num)
# count = 0
# lst = set()
# for i in range(m):
#     for j in range(i + 1, m + 1):
#         strs = num[i:j]
#         if strs in lst:
#             count += 1
# #         elif int(strs) % 22 == 0:
# #             count += 1
# # print(count)
#
# import sys
# num = sys.stdin.readline().strip()
# m = len(num)
# count = 0
# lst = set()
# for i in range(m - 1):
#     for j in range(i + 2, m + 1):
#         strs = num[i:j]
#         print(strs)
#         if strs in lst:
#             count += 1
#         elif int(strs) % 22 == 0:
#             count += 1
#             lst.add(strs)
# print(count)

# import sys
#
# line = sys.stdin.readline().strip()
# n, m, q = line.split()
# n, m, q = int(n), int(m), int(q)
# yuan_data_dic = {}
# for i in range(m):
#     l = sys.stdin.readline().strip()
#     a, b = l.split()
#     a, b = int(a), int(b)
#     yuan_data_dic[a] = yuan_data_dic.get(a, 0) + 1
#     yuan_data_dic[b] = yuan_data_dic.get(b, 0) + 1
#
# for j in range(q):
#     p = sys.stdin.readline().strip()
#     c, d = p.split()
#     c, d = int(c), int(d)
#     # print(yuan_data_dic)
#     yuan_data_dic[c], yuan_data_dic[d] = yuan_data_dic[d], yuan_data_dic[c]
#     # print(yuan_data_dic)
# result = ''
# res = list(yuan_data_dic.values())
# print(res)
# for k in range(len(res)):
#     if k > 0:
#         result += ' ' + str(res[k])
#     else:
#         result += str(res[k])
# print(result)

# import sys
# line = sys.stdin.readline().strip()
# n, m, q = line.split()
# n, m, q = int(n), int(m), int(q)
# yuan_data_dic = {}
# for i in range(m):
#     l = sys.stdin.readline().strip()
#     a, b = l.split()
#     a, b = int(a), int(b)
#     yuan_data_dic[a] = yuan_data_dic.get(a, 0) + 1
#     yuan_data_dic[b] = yuan_data_dic.get(b, 0) + 1
#
# for j in range(q):
#     p = sys.stdin.readline().strip()
#     c, d = p.split()
#     c, d = int(c), int(d)
# #     yuan_data_dic[c], yuan_data_dic[d] = yuan_data_dic[d], yuan_data_dic[c]
#
# import sys
# line = sys.stdin.readline().strip()
# n, m, q = line.split()
# n, m, q = int(n), int(m), int(q)
# yuan_data_dic = {}
# for i in range(m):
#     l = sys.stdin.readline().strip()
#     a, b = l.split()
#     a, b = int(a), int(b)
#     if a == b:
#         continue
#     yuan_data_dic[a] = yuan_data_dic.get(a, 0) + 1
#     yuan_data_dic[b] = yuan_data_dic.get(b, 0) + 1
#
# for j in range(q):
#     p = sys.stdin.readline().strip()
#     c, d = p.split()
#     c, d = int(c), int(d)
#     if c == d:
#         continue
#     yuan_data_dic[c], yuan_data_dic[d] = yuan_data_dic[d], yuan_data_dic[c]
#
# result = ''
# for k in range(1, n + 1):
#     print(' ', end = "")
#     print(yuan_data_dic[k], end = "")

# import sys
# n = int(sys.stdin.readline().strip())
# lst = []
# line = sys.stdin.readline().strip()
# lsts = line.split()
# for i in range(len(lsts)):
#     lst.append(int(lsts[i]))
# lst.sort()
# #
# new_lst = []
# l, r = 0, len(lst) - 1
# while l < r:
#     new_lst.append(lst[r])
#     new_lst.append(lst[l])
#     r -= 1
#     l += 1
# new_lst.append(lst[l])
# print(new_lst)
# #
# # left, right = 0, 1
# # res = 0
# # while right < len(new_lst):
# #     res += (abs(new_lst[right] - new_lst[left]))
# #     left += 1
# #     right += 1
# # print(res)
#
# import sys
# n = int(sys.stdin.readline().strip())
# line = sys.stdin.readline().strip()
# lsts = line.split()
# lst = []
# for i in range(len(lsts)):
#     lst.append(int(lsts[i]))
#
# def sub1(lst):
#     lst.sort()
#     used = [False] * len(lst)
#     return sub2(lst, used, [], [], len(lst), 0)
#
# def sub2(lst, used, path, res, size, level):
#     if size == level:
#         res.append(path[:])
#         return
#     for i in range(len(lst)):
#         if not used[i]:
#             if i > 0 and lst[i] ==lst[i - 1] and used[i - 1]== False:
#                 continue
#             path.append(lst[i])
#             used[i] = True
#             sub2(lst, used, path, res, size, level + 1)
#             path.pop(-1)
#             used[i] = False
#     return res
#
# full_res = sub1(lst)
# min_res = -float('inf')
# for i in range(len(full_res)):
#     new_lst = full_res[i]
#     left, right = 0, 1
#     res = 0
#     while right < len(new_lst):
#         res += (abs(new_lst[right] - new_lst[left]))
#         left += 1
#         right += 1
#     min_res = max(min_res, res)
# print(min_res)

# import sys
# line = sys.stdin.readline().strip()
# n, q = line.split()
# n, q = int(n), int(q)
# lst1 = []
# for i in range(n):
#     line1 = sys.stdin.readline().strip()
#     lst1.append(line1)
# print(3)
# print(1)

# # !/bin/python
# # -*- coding: utf8 -*-
# import sys
# import os
# import re
#
#
# class Solution:
#     def calcSumOfOnlyOne(self, arr):
#         yihuo = 0
#         for val in arr:
#             yihuo ^= val
#         pos = 1
#         while pos & yihuo == 0:
#             pos <<= 1
#         v1, v2 = 0, 0
#         for val1 in arr:
#             if val1 & pos:
#                 v1 ^= val1
#             else:
#                 v2 ^= val1
#         return v1 + v2
#
#
# _arr_cnt = 0
# _arr_cnt = int(input())
# _arr = list(map(int, input().split()))
#
# s = Solution()
# res = s.calcSumOfOnlyOne(_arr)

# print(str(res) + "\n")
# import sys
# import math
# n = int(sys.stdin.readline().strip())
# l, r, sums = 1, 2, 3
# while l < r and r <= (n + 1)//2:
#     if sums == n:
#         lst = [str(i) for i in range(l, r + 1)]
#         print(' '.join(lst))
#     if sums < n:
#         r += 1
#         sums += r
#     else:
#         sums -= l
# #         l += 1
# import sys
# line = sys.stdin.readline().strip()
# row, col = line.split()
# row, col = int(row), int(col)
#
# matrix =[]
# for i in range(row):
#     line = sys.stdin.readline().strip()
#     matrix.append(line)
#
# fangxiang = {'上':[-1, 0, '左', '右'], '下':[1, 0, '右', '左'], '左':[0, -1, '下', '上'], '右':[0, 1, '上', '下']}
# zhiling_num = int(sys.stdin.readline().strip())
# start = '上'
# x, y = 0, 0
# for u in range(len(matrix)):
#     for v in range(len(matrix[u])):
#         if matrix[u][v] == 'R':
#             x, y = u, v
# start_pos = [x, y]
#
# for j in range(zhiling_num):
#     zhiling = sys.stdin.readline().strip()
#     zhiling_split = zhiling.split()
#     if 'Forward' in zhiling:
#         for step in range(int(zhiling_split[-1])):
#             x1 = x + fangxiang[start][0]
#             y1 = y + fangxiang[start][1]
#             if 0 <= x1 < len(matrix) and 0 <= y1 < len(matrix[0]) and matrix[x1][y1] != 'O':
#                 x = x1
#                 y = y1
#             else:
#                 break
#     else:
#         if 'right' in zhiling:
#             start = fangxiang[start][3]
#         elif 'left' in zhiling:
#             start = fangxiang[start][2]
# end_pos = [x, y]
# print(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
#
# import sys
# num = int(sys.stdin.readline().strip())
# lst = sys.stdin.readline().strip()
# lst = lst.split()
# new_lst = []
# for i in range(num):
#     new_lst.append(int(lst[i]))
# a = new_lst[:]
# new_lst.sort()
#
# num1 = 0
# for j in range(num):
#     if a[j] != new_lst[j]:
#         num1 += 1
# print(num1 // 2)





#
#
# import sys
# import math
# n = int(sys.stdin.readline().strip())
# matrix = []
# for i in range(n):
#     line = sys.stdin.readline().strip()
#     matrix.append(list(map(int, line.split())))
#
# def sub(matrix, matrix1):
#     def new_matrix(matrix, x, y):
#         lst = []
#         for i in range(x, x + 2):
#             for j in range(y, y + 2):
#                 lst.append(matrix[i][j])
#         lst.sort()
#         return lst[-2]
#     for u in range(0, len(matrix), 2):
#         tmp = []
#         for v in range(0, len(matrix[0]), 2):
#             tmp.append(new_matrix(matrix, u, v))
#         matrix1.append(tmp)
#     return matrix1
#
# count = int(math.log(n, 2))
# for k in range(count):
#     matrix = sub(matrix, [])
# print(matrix[0][0])



# import sys
# line = int(sys.stdin.readline().strip())
# for i in range(line):
#     line1 = sys.stdin.readline().strip()
#     value = list(map(int, line1.split()))
#     a, b, c, x, y, z = value[0], value[1], value[2], value[3], value[4], value[5]
#     print(a,b,c,x,y,z)

# import sys
# line = int(sys.stdin.readline().strip())
#
# for i in range(line):
#     count = 0
#     line1 = sys.stdin.readline().strip()
#     start, end = list(map(int, line1.split()))
#     for j in range(start, end + 1):
# #         if '6' in str(j) and '8' in str(j):
# #             count += str(j).count('6')
# #     print(count)
#
#
# def workSchedule(n):
#     # write code here
#     lst = [1, 2, 4]
#     dp = [0] * (n + 1)
#     dp[0] = 1
#     for i in range(0, 3):
#         for j in range(1, n + 1):
#             start = 0
#             while lst[start] <= j and start < j:
#                 dp[j] = dp[j] + dp[j - lst[start]]
#                 start += 1
#         print("1",dp)
#     return dp
# print(workSchedule(10))



# import sys
# val_num = int(sys.stdin.readline().strip())
# line = sys.stdin.readline().strip()
# lst = list(map(int, line.split()))
#
# target = sum(lst) // 2
#
# class solu(object):
#     def __init__(self):
#         #self.res = []
#         self.count = 0
#     def sub1(self, lst, target ):
#         lst.sort()
#         self.sub2(0, lst, target, [])
#         return self.count
#     def sub2(self, start, lst, target, tmp):
#         if target == 0:
#             #self.res.append(tmp[:])
#             self.count += 1
#         if target < 0:
#             return
# #         for i in range(start, len(lst)):
#             tmp.append(lst[i])
#             self.sub2(i + 1, lst,  target - lst[i], tmp)
#             tmp.pop()
# print(solu().sub1(lst, target))


# import sys
# lst = sys.stdin.readline().strip()
# lst = list(map(int, lst.split(',')))
# m = len(lst)
# res_len = m + 1
# res = [0] * res_len
#
# xor1, xor2 = 0, 0
# for i in range(0, res_len - 1, 2):
#     xor1 ^= lst[i]
# for j in range(1, res_len + 1):
#     xor2 ^= j
#
# res[-1] = str(xor1 ^ xor2)
# for k in range(res_len - 2, -1, -1):
#     res[k] = str(lst[k] ^ int(res[k + 1]))
# print(','.join(res))
# import sys
# line = sys.stdin.readline().strip()
# lst = list(map(int, line.split(',')))
#
# m = len(lst)
# val_frq_dic = {}
#
# for i in range(m):
#     if lst[i] not in val_frq_dic:
#         val_frq_dic[lst[i]] = []
#     val_frq_dic[lst[i]].append(i)
# sort_val_lst = sorted(val_frq_dic, key=lambda x:len(val_frq_dic[x]), reverse= True)
# max_len = len(val_frq_dic[sort_val_lst[0]])
# res = float('inf')
# for val in sort_val_lst:
#     if len(val_frq_dic[val]) == max_len:
# #         res = min(res, val_frq_dic[val][-1] - val_frq_dic[val][0] + 1)
# # print(res)
#
#
# import sys
#
# strs = sys.stdin.readline().strip()
#
# fre_val_dic = {}
# for val in strs:
#     fre_val_dic[val] = fre_val_dic.get(val, 0) + 1
# max_val = max(list(fre_val_dic.values()))
# buket = [[] for _ in range(max_val + 1)]
# for i in fre_val_dic:
#     buket[fre_val_dic[i]].extend(i * fre_val_dic[i])
#
# for j in range(len(buket)):
#     if buket[j]:
#         buket[j] = sorted(buket[j])
#
# res = []
# for l in buket[::-1]:
#     if l:
#         res.extend(l)
# print(''.join(res))
# # # print(''.join([]))
#
#
# import sys
# line = sys.stdin.readline().strip()
# lst = []
# for i in range(len(line)):
#     if line[i] not in [',', '[', ']']:
#         lst.append(int(line[i]))
# k = int(sys.stdin.readline().strip())
#
# l, r = 0, len(lst) - 1
# dp = [0] * (k + 1)
# for i in range(1, k + 1):
#     if lst[l] >= lst[r]:
#         dp[i] = dp[i - 1] + lst[l]
#         l += 1
#     else:
#         dp[i] = dp[i - 1] + lst[r]
#         r -= 1
# print(dp[-1])



# import sys
# line = sys.stdin.readline().strip()
# lst = []
# indx = 0
# while indx < len(line):
#     if line[indx] in [',','[',']']:
#         indx += 1
#         continue
#     elif line[indx] == '-':
#         lst.append(int(line[indx] + line[indx + 1]))
#         indx += 2
#     else:
#         lst.append(int(line[indx]))
#         indx += 1





# k = int(sys.stdin.readline().strip())

# m = len(lst)
# class solution():
#     def sub(self, lst, start, end, k):
#         if k > end - start:
#             return sum(lst[start:end + 1])
#         if k <= 0:
#             return 0
#         res = max(self.sub(lst, start + 1, end, k - 1) + lst[start],
#                         self.sub(lst, start, end - 1, k - 1) + lst[end])
#         return res
# print(solution().sub(lst, 0, m - 1, k))
# import ast
# import sys
# line = sys.stdin.readline().strip()
# print(ast.literal_eval(line))
# # lst1 = []
# for j in range(len(lst)):
#     if lst[j] != ',':
#         lst1.append(int(lst[j]))
# print(lst1)
# lst2 = []
# indx = 0
# while indx < len(lst1):
#     lst2.append([lst1[indx], lst1[indx + 1]])
#     indx += 2
# print(lst2)
# lst2.sort(key = lambda x:x[1])     [[1,2][11,12]]
# visited = set()
# for start, end in lst2:
#     for d in range(start, end + 1):
#         if d not in visited:
#             visited.add(d)
#             break
# import sys
# line = sys.stdin.readline().strip()
# n , k = list(map(int, line.split()))
# line1 = sys.stdin.readline().strip()
# lst = list(map(int, line1.split()))
#
# if n == 1:
#     print(0)
# else:
#     res = 1
#     for i in range(len(lst) - 1):
#         res = min(res, abs(lst[i] - lst[i + 1]))
#     print(res)
# def maxEvents(events):
#     events.sort(key=lambda x: (x[1], x[0]))
#     # envelopes.sort(key=lambda d:(d[0],-d[1]))
#     visited = set()
#     max_val = 0
#     for s, e in events:
#         if max_val >= e:
#             continue
#         for day in range(s, e + 1):
#             if day not in visited:
#                 visited.add(day)
#                 max_val = day
#                 break
#     return events,visited
# print(maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]]))
# events= [[1,4],[4,4],[2,2],[3,4],[1,1]]
# events.sort(reverse = True)
# print(events)
# import heapq
# class Solution:
#     def maxEvents(self, events):
#         events.sort(reverse = True)
#         h = []
#         ans = 0
#         for i in range(1,100001):
#             while events and events[-1][0]==i:
#                 heapq.heappush(h,events.pop()[1])
#             while h:
#                 cur = heapq.heappop(h)
#                 if cur>=i:
#                     ans+=1
#                     break
#             print(i, ans)
#             if not events and not h:break
#         return ans
# print(Solution().maxEvents([[1,4],[4,4],[2,2],[1,3],[1,1]]))















#
#
# import sys
# floor_num = int(sys.stdin.readline().strip())
# line1 = sys.stdin.readline().strip()
# people_num = list(map(int, line1.split()))
# consum_value = []
# for i in range(floor_num):
#     line2 = sys.stdin.readline().strip()
#     a, b = list(map(int, line2.split()))
#     consum_value.append([a, b])
#
# res = float('inf')
# for i in range(floor_num):
#     tmp = 0
#     for j in range(len(consum_value)):
#         if j < i:
#             tmp += (consum_value[j][0]) * (i - j) * people_num[i]
#         elif j > i:
#             tmp += (consum_value[j][1]) * (j - i) * people_num[i]
#     res = min(res, tmp)
# print(res)

# import sys
# floor_num = int(sys.stdin.readline().strip())
# line1 = sys.stdin.readline().strip()
# people_num = list(map(int, line1.split()))
# consum_value = []
# for i in range(floor_num):
#     line2 = sys.stdin.readline().strip()
#     a, b = list(map(int, line2.split()))
#     consum_value.append([a, b])
#
# res = float('inf')
# for i in range(floor_num):
#     tmp = 0
#     for j in range(len(consum_value)):
#         if j < i:
#             tmp += (consum_value[j][0]) * (i - j) * people_num[i]
#         elif j > i:
#             tmp += (consum_value[j][1]) * (j - i) * people_num[i]
#     res = min(res, tmp)
# print(res)



# class Solution(object):
#     def __init__(self):
#         self.size = 0  ##控制树的重量
#         self.lst = []  ##以列表的形式实现树
#     def numIslands(self, grid):
#         m = len(grid)
#         n = len(grid[0])
#         self.size = m * n  ##目前的连通分量的数量
#         self.lst = [i for i in range(m * n)] ##初始树结构  每个的父节点都是本身
#         ocean = 0 ##海洋数量
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "0": ##海洋不连接 直接独自算作一个连通分量
#                     ocean += 1
#                 else:
#                     if i + 1 < m and grid[i + 1][j] == "1":
#                         self.union(n * i + j, n * (i + 1) + j)
#                     if j + 1 < n and grid[i][j + 1] == "1":
#                         self.union(n * i + j, n * i + (j + 1))
#         return self.size - ocean
#
#     def find(self, val):
#         while self.lst[val] != val:  ##找父节点，直到找到顶上的节点为止
#             val = self.lst[val]
#         return val
#
#     def union(self, a, b):
#         a_root = self.find(a)
# #         b_root = self.find(b)
# #         if a_root != b_root: ##处于未连通的状态
# #             self.lst[a_root] = b_root  ##连通上
# #             self.size -= 1  ##联通分量减1
# #         else:
#
#
#
# #             return
#
#
#
# import sys
#
# num = int(sys.stdin.readline().strip())
#
# def sub(strs):
#     fre_dic = {}
#     for val in strs:
#         fre_dic[val] = fre_dic.get(val, 0) + 1
#     val = list(fre_dic.values())
#     val.sort()
#     cha = val[1] - val[0]
#     for i in range(2, len(val)):
#         if val[i] - val[i - 1] != cha:
#             return 'No'
#     return 'Yes'
#
# for i in range(num):
#     strs = sys.stdin.readline().strip()
#     print(sub(strs))


# import sys
# line1 = sys.stdin.readline().strip()
# n, c1 = list(map(int, line1.split()))
# #
# # con_dic = {}
# # m = n * (n - 1) // 2
# # for i in range(m):
# #     line2 = sys.stdin.readline().strip()
# #     a, b, c = list(map(int, line2.split()))
# #     if a not in con_dic:
# #         con_dic[a] = []
#     con_dic[a].append(c)
#     if b not in con_dic:
#         con_dic[b] = []
#     con_dic[b].append(c)
#
# res = float('inf')
# for k in con_dic:
#     res = min(res, sum(con_dic[k]))
# print(res * c1)



# import sys
# line1 = sys.stdin.readline().strip()
# a, b, c = list(map(int, line1.split()))
# line2 = sys.stdin.readline().strip()
# zhu = line2.split()
# line3 = sys.stdin.readline().strip()
# wei = line3.split()
# line4 = sys.stdin.readline().strip()
# bin = line4.split()
# ju_num = int(sys.stdin.readline().strip())
#
#
# def judge(strs):
#     zhu_b, wei_b, bin_b = [], [], []
#     lst = strs.split()
#     for j in range(len(lst)):
#         if lst[j] in zhu:
#             zhu_b.append(j)
#         elif lst[j] in wei:
#             wei_b.append(j)
#         else:
#             bin_b.append(j)
#     if 0 not in zhu_b:
#         return 'NO'
#     if len(wei_b) > 1 or wei_b == []:
#         return 'NO'
#     for i in range(1, len(zhu_b)):
#         if zhu_b[i] != zhu_b[i - 1] + 1:
#             return 'NO'
#     if wei_b[0] < zhu_b[-1] or (bin_b != [] and wei_b[0] > bin_b[0]):
#         return 'NO'
#     if bin_b != []:
#         for k in range(1, len(bin_b)):
#             if bin_b[k] != bin_b[k - 1] + 1:
#                 return 'NO'
#     return 'YES'
#
#
#
# for i in range(ju_num):
#     line5 = sys.stdin.readline().strip()
# #     print(judge(line5))
#
# import sys
# nums = int(sys.stdin.readline().strip())
#
# def sub(matrix, lens, x, y):
#     res = 0
#     tmp = False
#     matrix_n = []
#     for i in range(lens):
#         for j in range(lens):
#             if matrix[x + i][y + j] != -1:
#                 matrix_n.append(matrix[x + i][y + j])
#                 res += matrix[x + i][y + j]
#             else:
#                 tmp = True
#                 break
#         if tmp == True:
#             break
#     print(matrix_n)
#     if tmp == True:
#         return 0
#     return res
#
# for i in range(nums):
#     line1 = sys.stdin.readline().strip()
#     n, m = list(map(int, line1.split()))
#     matrix = []
#     for i in range(n):
#         line2 = sys.stdin.readline().strip()
#         lst = list(map(int, line2.split()))
#         matrix.append(lst)
#
#     res = -float('inf')
#     for i in range(min(n, m)): ##正方形为i*i
#         for j in range(n):
#             for k in range(m):
#                 if matrix[j][k] != -1 and j + i <= n and k + i <= m:
#                     res = max(res, sub(matrix, i, j, k))
#     print(res)


# class Solution(object):
#     def firstMissingPositive(self, nums):
#         n = len(nums)
#         for i in range(n):
#             while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
#                 nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
#
#         for j in range(n):
#             if nums[j] != j + 1:
#                 return j + 1
#         return n + 1






# class Solution:
#     def generateTrees(self, n):
#         if(n==0):
#             return []
#         def build_Trees(left,right):
#             all_trees=[]  ##最终的结果
#             if(left>right):
#                 return [None]
#             for i in range(left,right+1): ##根为i
#                 left_trees=build_Trees(left,i-1)
#                 right_trees=build_Trees(i+1,right)
#                 for l in left_trees:
#                     for r in right_trees:
#                         cur_tree=TreeNode(i)
#                         cur_tree.left=l
#                         cur_tree.right=r
#                         all_trees.append(cur_tree)
#             return all_trees
#         res=build_Trees(1,n)
#         return res




# strs = ["flower","flow","flight"]
# ss = list(map(set, zip(*strs)))
# res = ""
# for i, x in enumerate(ss):
#     x = list(x)
#     if len(x) > 1:
#         break
#     res = res + x[0]
# print(res)


# def kmp(needle):
#     m = len(needle)
#     dp = [[0] * 20 for _ in range(m)]
#     dp[0][ord(needle[0]) - ord('a')] = 1
#     X = 0
#     for i in range(1, m):
#         for j in range(20):
#             if ord(needle[i]) - ord('a') == j:
#                 dp[i][j] = i + 1
#             else:
#                 dp[i][j] == dp[X][j]
#         X = dp[X][ord(needle[i]) - ord('a')]
#     return dp


# a = 'A'
#
# print(a.isalpha())





#
# def sum_24(lst):
#     if len(lst) == 1 and lst[0] == 24:
#         return True
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if sum_24([lst[i] + lst[j]] + lst[0:i] + lst[i + 1:j] + lst[j + 1:]):
#                 return True
#             if sum_24([lst[i] * lst[j]] + lst[0:i] + lst[i + 1:j] + lst[j + 1:]):
#                 return True
#             if lst[j] != 0 and sum_24([lst[i] / lst[j]] + lst[0:i] + lst[i + 1:j] + lst[j + 1:]):
#                 return True
#             if lst[i] != 0 and sum_24([lst[j] / lst[i]] + lst[0:i] + lst[i + 1:j] + lst[j + 1:]):
#                 return True
#             if sum_24([lst[i] - lst[j]] + lst[0:i] + lst[i + 1:j] + lst[j + 1:]):
#                 return True
#             if sum_24([lst[j] - lst[i]] + lst[0:i] + lst[i + 1:j] + lst[j + 1:]):
#                 return True
#     return False
# print(sum_24([1, 5, 6, 3]))


# # -*- coding:utf-8 -*-
# class Solution:
#     def GetLeastNumbers_Solution(self, tinput, k):
#         # write code here
#         if k > len(tinput) or k <= 0 or len(tinput) == 0:
#             return []
#         return self.bubble_rank(tinput)[:k]
#
#     def bubble_rank(self, tinput):
#         for i in range(len(tinput)):
#             for j in range(1, len(tinput) - i):
#                 if tinput[j] < tinput[j - 1]:
#                     tinput[j], tinput[j - 1] = tinput[j - 1], tinput[j]
#         return tinput









##快速排序、归并排序、堆排序冒泡排序、第k大的数
import random
def fast_rank(nums, start, end):
    if start >= end:
        return nums
    pivot = random.randint(start, end)
    nums[pivot], nums[start] = nums[start], nums[pivot]
    l = start
    r = end
    while l < r:
        while l < r and nums[r] >= nums[start]:
            r -= 1
        while l < r and nums[l] <= nums[start]:
            l += 1
        nums[l], nums[r] = nums[r], nums[l]
    nums[l], nums[start] = nums[start], nums[l]
    fast_rank(nums, start, l - 1)
    fast_rank(nums, l + 1, end)
    return nums
def rank1(lst):
    m = len(lst)
    return fast_rank(lst, 0, m - 1)
# print(rank1([3,5,7,9,1,3,4]))


def merge(left, right):
    l, r, res = 0, 0, []
    while len(left) > l and len(right) > r:
        if left[l] > right[r]:
            res.append(right[r])
            r += 1
        else:
            res.append(left[l])
            l += 1
    res += left[l:] + right[r:]
    return res
def splits(lst):
    m = len(lst)
    if m <= 1:
        return  lst
    mid = (0 + m) // 2
    left = splits(lst[:mid])
    right = splits(lst[mid:])
    return merge(left, right)
def merge_rank(lst):
    return splits(lst)
# print(merge_rank([3,5,7,9,1,3,4]))




def bubble_rank(lst):
    for i in range(len(lst)):
        for j in range(1, len(lst) - i):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
    return lst
# print(bubble_rank([3,5,7,9,1,3,4]))



def bubble_rank11(lst):
    m = len(lst)
    for i in range(m):
        for j in range(1, m - i):
            if lst[j - 1] > lst[j]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
    return lst
# print(bubble_rank11([5,4,7,3,2]))


# def ranks(tinput, start, temp, end):
#     i = start
#     j = 2 * start + 1
#     while j < end:
#         if j + 1 < end and tinput[j + 1] > tinput[j]:
#             j = j + 1
#         elif temp > tinput[j]:
#             break
#         else:
#             tinput[i] = tinput[j]
#             i = j
#             j = i * 2 + 1
#     tinput[i] = temp
#     return tinput
# def heap_rank(tinput):
#     end = len(tinput)
#     mid = end // 2
#     for i in range(mid, -1, -1):
#         tinput = ranks(tinput, i, tinput[i], end)
#     for j in range(len(tinput) - 1, 0, -1):
#         tinput[j], tinput[0] = tinput[0], tinput[j]
#         temp = tinput[0]
#         tinput = ranks(tinput, 0, temp, j)
#     return tinput
# print(heap_rank([3,5,7,9,1,3,4]))







# import sys
# import math
# line1 = sys.stdin.readline().strip()
# start, end = list(map(int, line1.split()))
#
# lst = []
# max_len = 0
# for i in range(start, end):
#     flag = 0
#     for j in range(2, int(math.sqrt(i)) + 1):
#         if i % j == 0:
#             flag = 1
#             break
#     if flag == 0:
#         lst.append(i)
#         max_len = max(max_len, len(str(i)))
# new_lst = []
# for k in range(len(lst)):
#     if len(str(lst[k])) < max_len:
#         a = '0' * (max_len - len(str(lst[k]))) + str(lst[k])
#         new_lst.append(a)
#     else:
#         new_lst.append(str(lst[k]))
# print(lst, new_lst)
# ge = 0
# shi = 0
# for u in range(len(new_lst)):
#     ge += int(new_lst[u][-1])
#     shi += int(new_lst[u][-2])
# print(min(ge, shi))



# A = [[1,0,0],[-1,0,5]]
# B = [[6,0,0],[0,0,0],[0,0,1]]
# B = list(zip(*B))
# res = []
# for i in range(len(A)):
#     hang = A[i]
#     tmp = []
#     for j in range(len(B)):
#         lie = list(B[j])
#         tmp += [sum([hang[k] * lie[k] for k in range(len(hang))])]
#     res.append(tmp[:])
# print(res)


# class Solution:
#     def minEditDistSubString(self, s1, s2):
#         # write code here
#         m, n = len(s1), len(s2)
#         l = 0
#         res = ''
#         min_len = float('inf')
#         while l <= m - n:
#             strs = s1[l:l + n]
#             tmp = self.sub(strs, s2)
#             print(tmp)
#             if tmp < min_len:
#                 min_len = tmp
#                 res = strs
#             l += 1
#         return res
#
#     def sub(self, s11, s22):
#         k = len(s11)
#         dp = [[0] * (k + 1) for _ in range(k + 1)]
#
#         for i in range(k + 1):
#             dp[i][0] = i
#             dp[0][i] = i
#         print(dp)
#         for u in range(1, k + 1):
#             for v in range(1, k + 1):
#                 if s11[u - 1] == s22[v - 1]:
#                     dp[u][v] = dp[u - 1][v - 1]
#                 else:
#                     dp[u][v] = min(dp[u - 1][v], dp[u][v - 1], dp[u - 1][v - 1]) + 1
#         return dp[k][k]
# s1 = "abcdefg"
# s2 = "bcfe"
# print(Solution().minEditDistSubString(s1, s2))


# class Solution(object):
#     def findWords(self, words):
#         lines = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
#         res = []
#         for i in range(len(words)):
#             strs = words[i]
#             if strs[0].lower() in lines[0]:
#                 tmp = 0
#             elif strs[0].lower() in lines[1]:
#                 tmp = 1
#             else:
#                 tmp = 2
#             print(tmp)
#             for j in range(1, len(strs)):
#                 if strs[j].lower() not in lines[tmp]:
#                     break
#             if j == len(strs) - 1 and strs[j] in lines[tmp]:
#                 res.append(words[i])
#         return res
# words = ["Hello","Alaska","Dad","Peace"]
# print(Solution().findWords(words))
#
#
# def decodeString(s):
#     nums = []
#     stack = []
#     for i in range(len(s)):
#         nums = []
#         stack = []
#         i = 0
#         while i < len(s):
#             if s[i].isdigit():
#                 r = ''
#                 while i < len(s) and s[i].isdigit():
#                     r += s[i]
#                     i += 1
#                 nums.append(int(r))
#             else:
#                 if s[i] == ']':
#                     tmp = []
#                     while stack and stack[-1] != '[':
#                         tmp.append(stack.pop())
#                     stack.pop()
#                     b = nums.pop()
#                     stack.append(''.join(tmp[::-1] * b))
#                     i += 1
#                 else:
#                     stack.append(s[i])
#                     i += 1
#     print(nums,stack)
#     return stack
# print(decodeString('100[leetcode]'))
#
#
#
# def wordPattern(pattern, s):
#     p_dic = {}
#     for i in range(len(pattern)):
#         if pattern[i] not in p_dic:
#             p_dic[pattern[i]] = []
#         p_dic[pattern[i]].append(i)
#
#     s_dic = {}
#     s = s.split()
#     for j in range(len(s)):
#         if s[j] not in s_dic:
#             s_dic[s[j]] = []
#         s_dic[s[j]].append(j)
#     print(p_dic.values())
#     print(s_dic.values())
#     return list(p_dic.values()) == list(s_dic.values())
# a = "abba"
# b = "dog cat cat dog"
# print(wordPattern(a, b))
# class Solution(object):
#     def __init__(self):
#         self.res = []
#     def s11(self, s1):
#         self.sub(s1, [], len(s1))
#         return len(self.res)
#
#     def sub(self, s1, tmp, lens):
#         if len(tmp) == lens:
#             self.res.append(''.join(tmp[:]))
#             return
#         for i in range(len(s1)):
#             tmp.append(s1[i])
#             self.sub(s1[:i] + s1[i + 1:], tmp, lens)
#             tmp.pop()
# # print(Solution().s11("abcdxabcde"))
#
# num1 = "11"
# num2 = "123"
# m = len(num1) - 1
# n = len(num2) - 1
# res = ''
# div = 0
# while m >= 0 and n >= 0:
#     div, mod = divmod(int(num1[m]) + int(num2[n]) + div, 10)
#     res += str(mod)
#     m -= 1
#     n -= 1
#
# res += num1[:m + 1][::-1]
# res += num2[: n + 1][::-1]
# print(res[::-1])
# nums = [2,-5,1,-4,3,-2]  #[2, -3, -2, -6, -3, -5]
# pre_sum = [nums[0]]
# for i in range(1, len(nums)):
#     pre_sum.append(pre_sum[-1] + nums[i])
# print(pre_sum)
#
# nums = [0] + nums
# for i in range(1, len(nums)):
#     nums[i] += nums[i - 1]
# print(nums)

# def countCharacters(words, chars):
#     res = '22'
#     char_dic = {}
#     for i in range(len(chars)):
#         char_dic[chars[i]] = char_dic.get(chars[i], 0) + 1
#
#     for j in range(len(words)):
#         tmp = char_dic.copy()
#         k = 0
#         while k < len(words[j]):
#             s = words[j][k]
#             if s in tmp:
#                 if tmp[s] != 0:
#                     tmp[s] -= 1
#                     k += 1
#                 else:
#                     break
#
#         if k == len(words[j]):
#             res += words[j]
#     return res
# words = ["cat","bt","hat","tree"]
# chars = "atach"
# print(countCharacters(words, chars))

# class Solution(object):
#     def equationsPossible(self, equations):
#
#         parent = [i for i in range(26)]
#         size = [1] * 26
#
#         def union(a, b):
#             roota = find(a)
#             rootb = find(b)
#             if roota == rootb:
#                 return
#             if size[roota] < size[rootb]:
#                 parent[roota] = rootb
#                 size[rootb] += size[roota]
#             else:
#                 parent[rootb] = roota
#                 size[roota] += size[rootb]
#
#         def find(a):
#             while parent[a] != a:
#                 # parent[a] = parent[parent[a]]
#                 a = parent[a]
#             return a
#
#         def connect(a, b):
#             roota = find(a)
#             rootb = find(b)
#             return rootb == roota
#
#         for i in range(len(equations)):
#             if equations[i][1] == '=':
#                 x = equations[i][0]
#                 y = equations[i][3]
#                 union(ord(x) - ord('a'), ord(y) - ord('a'))
#         for j in range(len(equations)):
#             if equations[j][1] == '!':
#                 x = equations[j][0]
#                 y = equations[j][3]
#                 if connect(ord(x) - ord('a'), ord(y) - ord('a')):
#                     return False
#         return True
#
# def diffWaysToCompute(expression):
#     if expression == []:
#         return [0]
#     res = []
#     for i in range(len(expression)):
#         if expression[i] in ['+', '-', '*']:
#             left = diffWaysToCompute(expression[:i])
#             right = diffWaysToCompute(expression[i + 1:])
#             for j in range(len(left)):
#                 for k in range(len(right)):
#                     if expression[i] == '+':
#                         res.append(left[j] + right[k])
#                     elif expression[i] == '-':
#                         res.append(left[j] - right[k])
#                     else:
#                         res.append(left[j] * right[k])
#     if res == []:
#         res.append(int(expression))
#         print("1", res)
#     return res
# expression = "4-1*2"
# print(diffWaysToCompute(expression))

# a = [[1, 2, 3], [0, 4, 5], [0, 0, 6]]
# for i in range(len(a)):
#     for j in range(i + 1, len(a[0])):
#         a[j][i] = a[i][j]
# print(a)

# # #去除停用词和停用词性
# import pandas as pd
# segandpos_result=pd.read_csv(r'D:\pythonProject\segandpos_result.csv',encoding='utf-8')
# with open(r'D:\pythonProject\without_stopwords_wordlist.txt', 'w', encoding='utf-8') as f1:
#     without_stopwords_wordlist = []
#     for i in range(len(segandpos_result)):
#         if segandpos_result['word'][i] in stop_words or segandpos_result['pos'][i] in stop_poss or segandpos_result['pos'][i]==None:
#             without_stopwords_wordlist.append('\n')
#         else:
#             without_stopwords_wordlist.append(segandpos_result['word'][i])
#     f1.write(' '.join(without_stopwords_wordlist))
#     f1.write('\n')
# a = ['经济', '\n', '经济', '论坛', '\n', '\n', '\n', '商业', '经济', '论坛']
# stack = []
# for i in range(1, len(a)):
#     if a[i] != '\n':
#         if a[i - 1] == '\n':
#             stack.append([a[i]])
#         else:
#             stack[-1].append(a[i])
# print(stack)
# res = ['\n']
# for i in range(len(a)):
#     if a[i] == '\n':
#         if res[-1] != '\n':  #要删除的词
#             res.append('\n')
#     elif a[i] != '\n':
#         if res[-1] != '\n':
#             res[-1].append(a[i])
#         else:
#             res.pop()
#             res.append([a[i]])
# print(res)

# numRows = 5
# res = [[1] * 1 for _ in range(numRows)]
# for i in range(1, numRows):
#     tmp = res[i - 1]
#     print(tmp)
#     for j in range(len(tmp) - 1):
#         res[i].append(tmp[j] + tmp[j + 1])
#     res[i].append(1)
# print(res)
# obstacleGrid = [[0,0],[1,1],[0,0]]
# m = len(obstacleGrid)
# n = len(obstacleGrid[0])
# for i in range(m):
#     if obstacleGrid[i][0] != 1:
#         obstacleGrid[i][0] = 1
#     else:
#         while i < m:
#             obstacleGrid[i][0] = 0
#             i += 1
#         break
#
# for j in range(1, n):
#     if obstacleGrid[0][j] != 1:
#         obstacleGrid[0][j] = 1
#     else:
#         while j < n:
#             obstacleGrid[0][j] = 0
#             j += 1
#         break
# print(obstacleGrid)
# import collections
# import heapq
# # k = 2
# nums = [1, 1, 2, 2, 2, 3]
# count = collections.Counter(nums)
# heap = [(val, key) for key, val in count.items()]
# print(heapq.nlargest(k, heap))
# a = [item[1] for item in heapq.nlargest(k, heap)]
# print(count)
# print(heap)
# val_fre_dic = collections.Counter()
# val_fre_lst = list(val_fre_dic.items())
# m = len(val_fre_lst)

# window = {1:1, 2:1, 3:1}
# window.pop(1)
# print(window)
# nums1 = [12,24,8,32]
# # nums2 = [13,25,32,11]
# # nums1.sort()
# # print(nums1)
# # res = []
# # for i in range(len(nums2)):
# #     for j in range(len(nums1)):
# #         if nums1[j] > nums2[i]:
# #             a = nums1.pop(j)
# #             res.append(a)
# #             break
# #     if j == len(nums1) - 1 and nums1[j] <= nums2[i]:
# #         b = nums1.pop(0)
# #         res.append(b)
# # print(res)
# import math
# a = math.sqrt(5)
# print(a)
# strs = ["eat","tea","tan","ate","nat","bat"]
# sort_val_dic = {}
# for v in strs:
#     tmp = sorted(v)
#
#     tmp = ''.join(tmp)
#     if tmp not in sort_val_dic:
#         sort_val_dic[tmp] = []
#     sort_val_dic[tmp].append(v)
# print(list(sort_val_dic.values()))
# nums = [2,7,11,15]
# val_indx_dic = {}
# for i in range(len(nums)):
#     if nums[i] not in val_indx_dic:
#         val_indx_dic[nums[i]] = []
#     val_indx_dic[nums[i]].append(i)
# print(val_indx_dic)



#
# import pandas as pd
# data1 = pd.read_excel(r'd:\大论文示例文件\法语术语处理\统计结果.xlsx', sheet_name='标注')
# data2 = pd.read_excel(r'd:\大论文示例文件\法语术语处理1\统计表格.xlsx', sheet_name='dr_cheng_dv')
# res = []
# for i in range(len(data2)):
#     tmp = []
#     for j in range(len(data1)):
#         if data2['term'][i] == data1['term'][j]:
#             tmp.append(data1['tag'][j])
#             break
#     if tmp == []:
#         res.append(2)
#     else:
#         res.append(tmp[0])
# res = pd.DataFrame(res, columns=['tag'])
# res.to_csv(r'D:\大论文示例文件\法语术语处理1\tag.csv', encoding='utf-8', header=False)


# import matplotlib  as mpl
# from matplotlib import pyplot as plt
# mpl.rcParams['axes.unicode_minus'] = False
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# # a = [7,7,8,8,9,9,9,10,10,10,10,11,11,12,13,14,14,15,15,15,16,16,16,17,17,17,18,18,18,19,19,19,19,20,20,20,20,21,21,21,22,22,23,24,1,2,3,4,5,6]
# # a = [7,7,8,8,9,9,9,10,10,10,10,11,11,12,13,14,14,15,15,15,16,16,16,16,17,17,17,17,18,18,18,18,19,19,19,19,20,20,20,21,21,21,22,22,23,24,1,2,3,4,5,6]
# a = [7,7,8,8,9,9,9,10,10,10,11,11,12,13,14,14,15,15,15,16,16,16,17,17,17,18,18,18,19,19,19,20,20,20,21,21,21,22,22,23,24,1,2,3,4,5,6]
# d = 1
# num_bins = (max(a) - min(a)) // d
# plt.hist(a, num_bins)
# plt.xticks(range(min(a), max(a) + d, d))
# plt.grid()
# plt.title('其他季节')
# plt.show()
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# m = len(height)
# left_max = [height[0]] + ([0] * (m - 1))
# for i in range(1, m):
#     if left_max[i - 1] < height[i]:
#         left_max[i] = height[i]
#     else:
#         left_max[i] = left_max[i - 1]
#
# right_max = ([0] * (m - 1)) + [height[-1]]
# for j in range(m - 2, -1, -1):
#     if right_max[j + 1] < height[j]:
#         right_max[j] = height[j]
#     else:
#         right_max[j] = right_max[j + 1]
# print(left_max, right_max)
# from nltk.stem import WordNetLemmatizer
# wl = WordNetLemmatizer()
# a = wl.lemmatize('actividades')
# print(a)
#
# from nltk.stem.porter import PorterStemmer
# porter_stemmer = PorterStemmer()
# porter_stemmer.stem()
#
# from nltk.stem import SnowballStemmer
# snowball_stemmer = SnowballStemmer('english')
# snowball_stemmer.stem()
# def a(s):
#     return len(s)
# print(a([1,2,3]))



# m = len(text1)
# n = len(text2)
# dp = [[0] * (m + 1) for _ in range(n + 1)]
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         if text1[j - 1] == text2[i - 1]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
# print(dp)  ##[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 1],
# [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1],
# [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1]]






# from sys import stdin
# num = int(stdin.readline().strip())
# lst = stdin.readline().strip().split()
# for i in range(len(lst)):
#     lst[i] = int(lst[i])
# lst = list(set(lst)).sort()
# print(lst)
# dp = [1] * num
# for i in range(1, num):
#     if lst[i] - lst[i - 1] > 1:
#         dp[i] = max(dp[:i])
#     else:
#         dp[i] = max(dp[: i - 1])
# print(dp[-1])



#
#
# from sys import stdin
# num = int(stdin.readline().strip())
# lst = stdin.readline().strip().split()
# for i in range(len(lst)):
#     lst[i] = int(lst[i])
# lst = list(set(lst))
# lst.sort()
#
# dp = [1] * num
# for i in range(1, num):
#     if lst[i] - lst[i - 1] > 1:
#         dp[i] = max(dp[:i]) + 1
#     elif i > 1:
#         dp[i] = max(dp[: i - 1]) + 1
# print(dp[-1])

# from sys import stdin
# num = int(stdin.readline().strip())
# lst = stdin.readline().strip().split()
# for i in range(len(lst)):
#     lst[i] = int(lst[i])
#
# def find(lst):
#     m = len(lst)
#     pre = lst[0]
#     res = lst[0]
#     for i in range(1, m):
#         pre = max(lst[i] + pre, lst[i])
#         res = max(res, pre)
#     return res
#
# res = -float('inf')
# for i in range(num):
#     for j in range(i + 1, num):
#         left = lst[:i]
#         mid = lst[i:j + 1][::-1]
#         right = lst[j + 1:]
#         tmp = left + mid +right
#         val = find(tmp)
#         res = max(res, val)
# print(res)


# from sys import stdin
# len, num = stdin.readline().strip().split()
# len = int(len)
# num = int(num)
# lst = stdin.readline().strip().split()
# lst = [int(v) for v in lst]
#
# res = []
# for j in range(num):
#     a = stdin.readline().strip().split()
#     a = [int(v) for v in a]
#     start = a[1] - 1
#     end = a[2] - 1
#     if a[0] == 1:
#         res.append((sum(lst[start:end + 1])))
#     else:
#         k = a[3]
#         for s in range(start, end + 1):
#             lst[s] += k
# print(sum(res))






'''
5 5
1 3 5 4 2
1 1 3
2 3 4 2
1 2 4
2 2 3 2
1 3 5
'''

# from sys import stdin
#
# len, num = stdin.readline().strip().split()
# len = int(len)
# num = int(num)
# lst = stdin.readline().strip().split()
# lst = [int(v) for v in lst]
#
# ##重排lst
# cha = [0] * len
# jia = [0] * len
# cao_zuo = []
# for j in range(num):
#     a = stdin.readline().strip().split()
#     a = [int(v) for v in a]
#     cao_zuo.append(a)
#     start = a[1] - 1
#     end = a[2] - 1
#     if a[0] == 1:  # 查询
#         for k in range(start, end + 1):
#             cha[k] += 1
#     else:
#         a3 = a[3]
#         for d in range(start, end + 1):
#             jia[d] += a3
#
# stack = sorted(lst)
# tmp = [cha[i] + jia[i] for i in range(len)]
#
# new_lst = [0] * len
# used = [False] * len
# while used != [True] * len:
#     max_val = -float('inf')
#     for k in range(len(used)):
#         if used[k] == False:
#             max_val = max(max_val)
#
#     indx = tmp.index(max_val)
#     if used[indx] == False:
#         new_lst[indx] = stack.pop(-1)
#     used[indx] = True
#
# res = []
# for j in range(num):
#     a = cao_zuo[j]
#     start = a[1] - 1
#     end = a[2] - 1
#     if a[0] == 1:
#         res.append((sum(new_lst[start:end + 1])))
#     else:
#         k = a[3]
#         for s in range(start, end + 1):
#             new_lst[s] += k
# print(sum(res))

# a = [1,2,3,4,5]
# b = [1,4,7,4,1]
# #c = [2,4,5,3,1]
# new_lst = [0] * len(a)
# for i in range(len(a)):
#     max_val = max(b)
#     max_indx = b.index(max_val)
#     new_lst[max_indx] = a.pop()
#     b[max_indx] = -float('inf')
# print(new_lst)

# line1 = sys.stdin.readline().strip()
# value = list(map(int, line1.split()))

#
# def GetSubArrayMaxProduct(self, nums):
#     # write code here
#     m = len(nums)
#     min_val = nums[0]
#     max_val = nums[0]
#     res = max_val
#     for i in range(1, m):
#         min_val, max_val = min(nums[i], nums[i] * min_val, nums[i] * max_val), max(nums[i], nums[i] * min_val,
#                                                                                    nums[i] * max_val)
#         res = max(res, max_val)
#     return res

# def calDPDScore(self, dpdInfo):
#     # write code here
#     dpdInfo += 'N'
#     m = len(dpdInfo)
#     l, r = 0, 0
#     res = 0
#     while r < m:
#         if dpdInfo[r] == 'N':
#             res = max(res, r - l)
#             r += 1
#             l = r
#         else:
#             r += 1
#     if res == 0:
#         return 0
#     if 0 < res <= 3:
#         return -10
#     elif 3 < res <= 7:
#         return -15
#     else:
#         return -25
# class Solution:
#     def __init__(self):
#         self.res = float('inf')
#     def GetMinCalculateCount(self, sourceX, sourceY, targetX, targetY):
#         # write code here
#         self.sub(sourceX, sourceY, targetX, targetY, 0)
#         return self.res if self.res != float('inf') else -1
#
#     def sub(self, s, t, x, y, tmp):
#         if s == x and t == y:
#             self.res = min(self.res, tmp)
#             return
#         if s > x or t > y:
#             return
#         self.sub(s + 1, t + 1, x, y, tmp + 1)
#         self.sub(s * 2, t * 2, x, y, tmp + 1)
#
# print(Solution().GetMinCalculateCount(10,100,22,202))

##乘积最大子数组,用户账单逾期扣分(最大连续字符)，最少计算次数














# res = []
# def three_sum(lst, tmp):
#     if len(tmp) == 3:
#         res.append(sum(tmp[:]))
#         return
#     for i in range(len(lst)):
#         tmp.append(lst[i])
#         three_sum(lst[i + 1:], tmp)
#         tmp.pop()
#
# lst = [1, 2, 3, 4, 6, 7]
# lst.sort()
# three_sum(lst, [])
# nums = 0
# for i in range(len(res)):
#     if res[i] in lst:
#         nums += 1
# print(nums)




# lst = [[2, 2], [0, 4], [1, 2], [5, 6]]
# lst.sort(key = lambda x:x[0])
# new_lst = [lst[i][1] for i in range(len(lst))]
# nums = 0
# m = len(new_lst)
# for i in range(m):
#     for j in range(i + 1, m):
#         if new_lst[j] > new_lst[i]:
#             nums += 1
# print(nums)


# class Solution(object):
#     def __init__(self):
#         self.res = []
#
#     def generateParenthesis(self, n):
#         self.sub_generate(n, n, '')
#         return self.res
#
#     def sub_generate(self, left_n, right_n, tmp):
#         if left_n < right_n:
#             return
#         if left_n == right_n == 0:
#             self.res.append(tmp)
#             return
#         self.sub_generate(left_n - 1, right_n, tmp + '(')
#         self.sub_generate(left_n, right_n - 1, tmp + ')')
# print(Solution().generateParenthesis(3))












# ##最长连续递增子序列
#
# lst = [1,3,2,6,7,9]
# m = len(lst)
# l, r = 0, 1
# lens = 0
# while r < m:
#     if lst[r] > lst[l]:
# #         r += 1
# #         lens
#
#
#
# from sys import stdin
# def judge(strs):
#     strs += '='
#     strs = list(strs)
#     print(strs)
#     lst = []
#     m = len(strs)
#     indx = 0
#     tmp = ''
#     while indx < m:
#         if strs[indx] in ['=', '<', '>']:
#             lst.append(tmp)
#             tmp = ''
#             lst.append(strs[indx])
#         else:
#             tmp += strs[indx]
#         indx += 1
#     lst = lst[:-1]
#     res = ''
#     for i in range(len(lst)):
#         if lst[i] not in ['=', '<', '>']:
#             res += lst[i].strip()
# #         else:
# #             res += ' ' + lst[i] + ' '
# #     return res
# # a = stdin.readline().strip()
# # print(judge(a))
#
#
#
#
# from sys import stdin
# t = int(stdin.readline().strip())
# for i in range(t):
#     strs = stdin.readline().strip()
#     a, b = strs.split()
#     a = int(a)
#     lst = []
#     for i in range(len(b)):
#         lst.append(a * int(b[i]))
#     print(sum(lst))
#
# from sys import stdin
# m = int(stdin.readline().strip())
# lst = stdin.readline().strip().split()
# lst = [int(v) for v in lst]
#
# def sub(lst, nums, tmp, start):
#     if len(tmp) == nums:
#         mul = 1
#         for k in tmp:
#             mul *= k
#         zuhe[mul] = zuhe.get(mul, 0) + 1
#         return
#     for i in range(start, len(lst)):
#         tmp.append(lst[i])
#         sub(lst, nums, tmp, i + 1)
#         tmp.pop()
#
# zuhe = {}
# # for i in range(1, m + 1):
# #     sub(lst, i, [], 0)
# # print(zuhe)
# from sys import stdin
# m = int(stdin.readline().strip())
# lst = stdin.readline().strip().split()
# lst = [int(v) for v in lst]
#
# def sub(lst, nums, tmp, start):
#     if len(tmp) == nums:
#         mul = 1
#         for k in tmp:
#             mul *= k
#         zuhe[mul] = zuhe.get(mul, 0) + 1
#         return
#     for i in range(start, len(lst)):
#         tmp.append(lst[i])
#         sub(lst, nums, tmp, i + 1)
#         tmp.pop()
#
# zuhe = {}
# for i in range(1, m + 1):
#     sub(lst, i, [], 0)
#
# def zhiyinshu(nums):
#     res = set()
#     for i in range(2, nums + 1):
#         while nums % i == 0:
#             res.add(i)
#             nums /= i
#     return len(res)
#
# end_res = 0
# for u in zuhe:
#     n = zhiyinshu(u)
#     end_res += n * zuhe[u]
# print(end_res)

# from sys import stdin
# a, b = stdin.readline().strip().split()
# y, m, d = stdin.readline().strip().split()
# strs = y + m + d
# strs = list(strs)
# m1 = len(strs)
# l, r = 0, m1 - 1
# while l < r:
#     if strs[l] == strs[r]:
#         l += 1
#         r -= 1
#     else:
#         strs[r] = strs[l]
# print(''.join(strs[:len(y)]) + ' ' + ''.join(strs[len(y):len(y) + len(m)]) + ' ' + ''.join(strs[len(y) + len(m):]))



# # import sys
# # line1 = sys.stdin.readline().strip()
# # a, b, c = list(map(int, line1.split()))
#
#
#
#
#
#
#
#
#
#
# from sys import stdin
# m1 = int(stdin.readline().strip())
# lst = list(map(int, stdin.readline().strip().split()))
# indx = 0
# new_lst = []
# while indx < m1:
#     tmp0 = 0
#     tmp1 = 0
#     if lst[indx] == 0:
#         while indx < m1 and lst[indx] == 0:
#             tmp0 += 1
#             indx += 1
#         new_lst.append((tmp0, 0))
#     else:
#         while indx < m1 and lst[indx] == 1:
#             tmp1 += 1
#             indx += 1
#         new_lst.append((tmp1, 1))
# # res = 0
# # for j in range(len(new_lst)):
#
#
# def sums(new_lst, m):
#     res = 0
#     for i in range(0, m, 2):
#
#         if i + 3 < m:
#             a = [new_lst[k][0] for k in range(i, i + 3)]
#             res = max(res, sum(a))
#         else:
#             b = [new_lst[k1][0] for k1 in range(i, m)]
#             res = max(res, sum(b))
#     return res
#
# m = len(new_lst)
# tmp1 = sums(new_lst, m)
# res = sums(new_lst[1:], m - 1)
# print(max(tmp1, res))
#
#
# from sys import stdin
# m, n, k = list(map(int, stdin.readline().strip().split()))
# dp = [[1] * n for _ in range(m)]
# for i in range(k):
#     x, y = list(map(int, stdin.readline().strip().split()))
#     dp[x - 1][y - 1] = 0
#     if x - 1 == 0:
#         for j in range(y, n):
#             dp[0][j] = 0
#     elif y - 1 == 0:
#         for k in range(x, m):
#             dp[k][0] = 0
# print(dp)
# mo = 10 ** 9 + 7
# for i in range(1, m):
#     for j in range(1, n):
#         if dp[i][j] != 0:
#             dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
# print(dp[m - 1][n - 1] % mo)


# from sys import stdin
# lens = int(stdin.readline().strip())
# lst = list(map(int, stdin.readline().strip().split()))
# left_max = [lst[0]]
# for i in range(1, lens):
#     if left_max[-1] < lst[i]:
#         left_max.append(lst[i])
#     else:
#         left_max.append(left_max[-1])
# right_max = [lst[-1]]
# for j in range(lens - 2, -1, -1):
#     if right_max[-1] < lst[j]:
#         right_max.append(lst[j])
#     else:
#         right_max.append(right_max[-1])
# right_max = right_max[::-1]
# res = []
# for k in range(lens):
#     if lst[k] < min(left_max[k], right_max[k]):
#         res.append(1)
#     else:
#         res.append(0)
# dp = [res[0]]
# for u in range(1, lens):
#     if res[u] == 0:
#         dp.append(0)
#     else:
#         dp.append(dp[-1] + 1)
# print(max(dp))
# print(res)

'''
12
0 1 0 2 1 0 1 3 2 1 2 1
'''

##[5,1,2,1,5]
# from sys import stdin
# lens = int(stdin.readline().strip())
# lst = list(map(int, stdin.readline().strip().split()))
# def sub(lst, val):
#     indx = 0
#     res = 0
#     val = val
#     while indx < len(lst):
#         if lst[indx] < val:
#             res += 1
#             val = lst[indx]
#         else:
#             break
#         indx += 1
#     return res
# res = 0
# for i in range(lens):
#     left = lst[:i][::-1]
#     right = lst[i + 1:]
#     res = max(res, sub(left, lst[i]) + sub(right, lst[i]))
# print(res)

# def lengthOfLastWord(s):
#     s = s.strip()
#     print(s)
#     m = len(s)
#     res = 0
#     l, r = m - 1, m - 1
#     while l >= 0:
#         if s[l] != " ":
#             l -= 1
#         else:
#             res = r - l
#             break
#     print(l, r)
#     return res
# print(lengthOfLastWord('Hello World'))


##最长递增子序
class Node(object):
    def __init__(self, item):
        self.item = item  # 表示对应的元素
        self.left = None  # 表示左节点
        self.right = None  # 表示右节点

class Tree(object):
    def __init__(self):
        self.root = Node('root')  # 根节点定义为 root 永不删除，作为哨兵使用。

    def add(self, item):  ##增加元素
        node = Node(item)
        if self.root is None:  # 如果二叉树为空，那么生成的二叉树最终为新插入树的点
            self.root = node
        else:
            q = [self.root]  # 将q列表，添加二叉树的根节点
            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:  # 左子树为空则将点添加到左子树
                    pop_node.left = node
                    return
                elif pop_node.right is None:  # 右子树为空则将点添加到右子树
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def delete(self, item): ##删除节点item是什么，应该是值，不是指的节点
        if self.root is None:  # 如果根为空，就什么也不做
            return False
        parent = self.get_parent(item)
        if parent:
            if parent.left.item == item:
                del_node = parent.left
            else:
                del_node = parent.right  # 待删除节点
            if del_node.left is None:
                if parent.left.item == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                return True
            elif del_node.right is None:
                if parent.left.item == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left
                del del_node
                return True
            else:  # 左右子树都不为空
                tmp_pre = del_node
                tmp_next = del_node.right
                if tmp_next.left is None:   ##右子树上去
                    # 替代
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                else:   ##最左边的子树上去
                    while tmp_next.left:  # 让tmp指向右子树的最后一个叶子
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # 替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                if parent.left.item == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False

    def get_parent(self, item):  ##得到父节点
        if self.root.item == item:
            return None  # 根节点没有父节点
        tmp = [self.root]  # 将tmp列表，添加二叉树的根节点
        while tmp:
            pop_node = tmp.pop(0)
            if pop_node.left and pop_node.left.item == item:  # 某点的左子树为寻找的点
                return pop_node  # 返回某点，即为寻找点的父节点
            if pop_node.right and pop_node.right.item == item:  # 某点的右子树为寻找的点
                return pop_node  # 返回某点，即为寻找点的父节点
            if pop_node.left is not None:  # 添加tmp 元素
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)
        return None


def Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def Tree(object):
    def __init__(self):
        self.root = Node('root')

    def add(self, item):
        node = Node(item)
        if not self.root:
            self.root = node
        else:
            queue = [self.root]
            while queue:
                tmp = queue.pop(0)
                if tmp.left == None:
                    tmp.left = node
                    return
                elif tmp.right == None:
                    tmp.right = node
                    return
                else:
                    queue.append(tmp.left)
                    queue.append(tmp.right)

    def delete(self, item):
        if not self.root:
            return False
        parent = self.parent(item)
        if not parent:
            return False
        if parent.left.val == item:
            del_node = parent.left
        else:
            del_node = parent.right
        if del_node.left == None:
            if parent.left.val == item:
                parent.left = del_node.right
            else:
                parent.right = del_node.right
            del del_node
            return True
        elif del_node.right == None:
            if parent.left.val == item:
                parent.left = del_node
            else:
                parent.right = del_node
            del del_node
            return True
        else:
            tmp = del_node
            nxt = del_node.right
            if nxt.left == None:
                tmp.right = nxt.right
                nxt.left = del_node.left
                nxt.right = del_node.right
            else:
                while nxt.left:
                    tmp = nxt
                    nxt = nxt.left
                tmp.left = nxt.right
                nxt.left = del_node.left
                nxt.right = del_node.right
            if parent.left.val == item:
                parent.left = nxt
            else:
                parent.right = nxt
            del del_node
            return True

    def parent(self, item):
        if self.root.val == item:
            return None
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left and node.left.val == item:
                return node
            elif node.right and node.right.val == item:
                return node
            else:
                queue.append(node.left)
                queue.append(node.right)
        return None

#CalPiV2.py
# from random import random
# DARTS = 1000 * 1000 * 100 ##总点数
# hits = 0.0 ##落在圆內的点数
# for i in range(1, DARTS+1):
#     x, y = random(), random()
#     dist = pow(x ** 2 + y ** 2, 0.5)
#     if dist <= 1.0:
#         hits = hits + 1
# pi = 4 * (hits / DARTS)
# print("圆周率值是: {}".format(pi))

def longestCommonSubsequence(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [0] * n
    for i in range(m):
        left_top = 0
        for j in range(n):
            tmp = dp[j]
            if text1[i] == text2[j]:
                dp[j] = left_top + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            left_top = tmp
        print(dp)
    return True
text1 = "ezupkr"
text2 = "ubmrapg"
# print(longestCommonSubsequence(text1, text2))



def longestCommonSubsequence1(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [0] * (n + 1)
    for i in range(1, m + 1):
        left_top = 0
        for j in range(1, n + 1):
            tmp = dp[j]
            if text1[i - 1] == text2[j - 1]:
                dp[j] = left_top + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            left_top = tmp
        print(dp)
    return True
print(longestCommonSubsequence1(text1, text2))