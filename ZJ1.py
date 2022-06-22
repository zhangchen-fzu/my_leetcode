# a=-3
# print(bin(-3))
# b=-3&0xffffffff
# print(bin(b))pr
# a=bin(3)

# def dd(n):
#     ret = 1
#     x = 4
#     while (n):
#         if (n&1):
#             ret*=x
#         x*=x
#         n>>=1
#     return ret
# print(dd(3))

# class Solution:
#     def HasSubtree(self, pRoot1, pRoot2):
#         # write code here
#         result=False
#         if pRoot1 and pRoot2:
#             if pRoot1.val==pRoot2.val:
#                 result=self.sames(pRoot1,pRoot2)
#             if not result:
#                 result=self.HasSubtree(pRoot1.left,pRoot2)
#             if not result:
#                 result=self.HasSubtree(pRoot1.right,pRoot2)
#         return result
#     def sames(self,p1,p2):
#         if not p1:
#             return False
#         if not p2:
#             return True
#         return p1.val==p2.val and self.sames(p1.left,p2.left) and self.sames(p1.right,p2.right)
#
#
# sequence=[]
# root=sequence[-1]
# index=0
# for i in range(len(sequence)):
#     if sequence[i]>root:
#         index=i
#         break
# print(index)
# sequence=[]
# root=sequence[-1]
# i = 0
# while i < len(sequence) - 1:
#     if sequence[i] > root:
#         break
#     i += 1
# print(i)
# a=[]
# b=[]
# b.append('adsd')
# a.append(b)
# print(a)
# right=[4]
# # root=4
# # result=all(j>root for j in right)
# # print(result)
# ss='fwedwdfvdrf'
# print(ss)
# ss=list(ss)
# ss[1],ss[2]=ss[2],ss[1]
# ss=''.join(ss)
# print(ss)
# ss=list(ss)
# ss[1],ss[2]=ss[2],ss[1]
# ss=''.join(ss)
# print(ss)
# a=["aab","aba","baa"]
# print(sorted(list(set(a))))
# a=[1,1,2,3,4,5,3]
# for i in a:
#     if i<3:
#      print(i)
# print("\n")
# for i in range(len(a)):
#     if a[i] < 3:
#         print(a[i])
# a=[1,2,3]
# print(max(a))
# n=1234561
# a=['1','2','3','4','7','0','8','9','5','6']
# a.sort()
# print(a)
# s='google'
# result={}
# new_s=list(s)
# for i in new_s:
#     result[i]=s.count(i)
# print(result)
# val=-1
# for j in result:
#     if result[j]==1:
#         val=s.index(j)
#         break
#     else:
#         continue
# print(val)
# a={'g':[(2,0)]}
# print(a)
# import collections
# queue=collections.deque()
# queue.append(1)
# queue.append(2)
# print(queue)
# print(len(queue))
# print(abs(2-1)<=1)
# array=[1,2,3,4,3,2,1,5,7,7]
# XORsum = 0
# for num in array:
#     XORsum ^= num
# # print(XORsum)
# array=[1,2,3,4,3,2,1,5,7,7]
# pos=1
# ans1 = 0
# ans2 = 0
# for num in array:
#     if num & pos == 0:
#         ans1 ^= num
#     else:
#         ans2 ^= num
# print([ans1, ans2] if ans1 < ans2 else [ans2, ans1])
# array=[1,2,3,4,3,2,1,5,7,7]
# for i in array:
#     print(i&1)
# print(2^3)
# a='abcXYZdef'
# print(len(a))
# left=a[:3]
# right=a[3:]
# print(left,right,right+left)
# s='dw wef fwfwe  wefe'
# # # print(list(s))
# num1=0
# num2=0
# if num1==0 or num2==0:
#     print(num1 or num2)
# print(bin((-2^1)&0xffffffff))
# print(bin(((-2)&0xffffffff)^1))
# print(bin(-2&0xffffffff&0x7fffffff))
# # print(~(2&0x7fffffff))
# # print(bin(-2&0x7fffffff))
# # print(1&0x7fffffff)
# # print(0x7fffffff)
# # # print((1&2)&0xffffffff)
# a=0xFFFFFFFF
# n1=-10
# n2=2
# cou=0
# # print(bin(n1))
# # print(bin(n2))
# # print(bin(n1^n2))
# # print(bin(n1&n2))
# # print(bin((n1^n2)&a))
# # print(bin((n1&n2)&a))
# while n2 != 0:
#     cou+=1
#     n1, n2 = (n1 ^ n2), ((n1 & n2) << 1)
#     n1 = n1 & a
#     n2 = n2 & a
#     print("n2",n2)
# print(bin(n1))
# print(cou)
# # print(bin(n1^a))
# print(bin(~(n1^a)))
# print(bin(-2^4))
# # print(bin((-2^4)&a))
# # print(bin(((-2^4)&a)^a))
# # print(bin(~(((-2^4)&a)^a)))
# # print(~(((-2^4)&a)^a))
# print(bin(-10))
# print(bin(2))
# b=(-10^2)
# c=(-10&2)<<1
# print(bin(b))
# print(bin(c))
# d=b&a
# e=c&a
# print(bin(d))
# print(bin(e))
# f=(d^e)
# g=(d&e)<<1
# print(bin(f))
# print(bin((g)))
# h=f&a
# i=g&a
# print(bin(h))
# print(bin(i))
# j=h^i
# k=h&i
# print(bin(j))
# print(bin(k))
# print(bin((-1^2)&a))
# print(-4^5)
# print(bin((-10^2)))
# import numpy as np
# a=[1,2,3,4,5]
# print(2*np.prod(a))
# a=[1,2]
# b=[2,3]
# print(a*b)
# str='aaabccd'
# pattern='a*abc*d'
# len1=len(str)
# len2=len(pattern)
# dp = [[False]*(len2+1) for _ in range(len1+1)]
# dp[0][0] = True
# for j in range(2, len2+1, 2):
#     dp[0][j] = dp[0][j - 2] and pattern[j - 1] == '*'
# print(dp)
# str='100'
# if str.count('.')>1:
#     print("False3")
# if '-.' or '.-' or '+.' or '.+' in str:
#     print("False4")
# if 'e' in str or 'E' in str:
#     inx=str.index('e') or str.index('E')
#     left=str[:inx]
#     if left==[]:
#         print("False5")
#     right=str[inx+1:]
#     if right==[] or '.' in right:
#         print("False")
#     # left_res=self.isNumeric(left)
#     # right_res=self.isNumeric(right)
#     # return left_res and right_res
# for i in range(len(str)):
#     if i==0 and str[i]=='.':
#         print("False1")
#     if i==0 and str[i]=="+":
#         continue
#     elif i==0 and str=='-':
#         continue
#     else:
#         if str[i]=='.':
#              continue
#         n=ord(str[i])-ord('0')
#         if n<0 or n>9:
#             print("False2")
# print("True")
# str='+e3'
# a=float(str)
# print(a)
# str='1e+'
# eindex=1
# print([str[2]])
# print(str[eindex+1:])
# if [str[2]]==str[eindex+1:]:
#     print("shi")
# str='-2.e2'
# # lens=len(str)
# # print(lens)
# # for i in range(len(str)):
# #     print(str[i],type(str[i]))
# # eindex=str.index('e') or str.index('E')
# # print(eindex)
# a=float(str)
# print(a)
# a=[11,12,13]
# # print(a.pop(0))
# # # print(a)
# a=[1,2,3,4,5]
# print(a.pop())
# a=[2,3]
# order=sorted(a)
# lens=len(order)
# if lens%2==0:
#     print((order[int(lens/2)]+order[int(lens/2)-1])/2)
# else:
#     print(order[lens//2])
# import heapq
# # items=[-3,-2,1,-4]
# # # a=heapq.heappop(items)
# # # print(a,items)
# # print(items[:4])
# import numpy as np
# a=np.array([['a','b','c','e'],['s','f','c','s'],['a','d','e','e']])
# print(a.shape[0])
# if not 0:
#     print("0")
# if not 1:
# res={'w':2}
# res['a']=res.get('a',0)+1
# print(res)
# assis=[i for i in range(1,5)]
# print(assis)
# a="asasd   asda  asd asda"
# b=a.split()
# print(' '.join(b))
# c=a.split(' ')
# print(c)
# s='a78789'
# i=0
# if i==0 and s[0]=='-':
#     print('shi')
# else:
#     print('fou')
# print(max([1,13],[5,6]))
# res=[[1,4]]
# last=res[-1]
# last[1]=2
# print(res)
# left=9
# piles=9
# if left==piles:
#     piles+=1
# print(left)
# a = input("input:")
# from sys import stdin
# import math
# while True:
#     a=stdin.readline().strip()
#     n,m=a.split(' ')
#     n=int(n)
#     m=int(m)
#     res=n
#     for _ in range(m-1):
#         n=math.sqrt(n)
#         res+=n
#     print('%.2f'%res)
# a=['1','2','3']
# # a=str(a)
# # print(' '.join(a))
# from sys import stdin
# aa=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# m=0
# n=0
# while True:
#     a=stdin.readline().strip()
#     if ' ' in a:
#         m,n=a.split(' ')
#         m=int(m)
#         n=int(n)
#     print(m,n)
#     if ' ' not in a:
#         val=int(a)
#         if val%n!=0:
#             print(aa[val//n],end='')
#             print(val%n)
#             # print('\n')
#         else:
#             print(aa[(val//n)-1],end='')
#             print(5)
#             # print('\n')
# from sys import stdin
# res=''
# n=0
# aa='abcdefghijklmnopqrstuvwxyz'
# aaa=list(aa)
# b=stdin.readline().strip()
# res+=b
# res=list(res)
# aa=stdin.readline().strip()
# n=int(aa)
# while True:
#     a=stdin.readline().strip()
#     if ' ' in a:
#         left,right,k=a.split(' ')
#         left=int(left)
#         right=int(right)
#         k=int(k)
#         for i in range(left-1,right):
#             ind=aaa.index(res[i])
#             ind=ind-k
#             if ind<0:
#                 res[i]=aaa[len(aaa)+ind]
# #             else:
# #                 res[i]=aaa[ind]
# from sys import stdin
# res=''
# res+=stdin.readline().strip()
# res=list(res)
# b=stdin.readline().strip()
# # n=int(b)
# # aa='abcdefghijklmnopqrstuvwxyz'
# # aaa=list(aa)
# # while n!=0:
# #     a=stdin.readline().strip()
# #     left,right,k=a.split(' ')
# #     left=int(left)
# #     right=int(right)
# #     k=int(k)
# #     for i in range(left-1,right):
# #         ind=aaa.index(res[i])
# #         ind=ind-k
# #         if ind<0:
# #             res[i]=aaa[len(aaa)+ind]
# #         else:
# #             res[i]=aaa[ind]
# #     n-=1
# # print(''.join(res))
from collections import Counter
# def sample(n, cnt):
#     i = 0
#     table = []
#     z = sum(num ** 0.75 for num in cnt)  # denominator
#     prob = cnt[i] ** 0.75 / z  # cumulative probability
#     for a in range(n):
#         table.append(i)
#         if a > prob * n:
#             i += 1
#             prob += cnt[i] ** 0.75 / z
#     return table
# cnt = [1, 2, 3, 100, 15]
# print(sample(34, cnt))
# n=4
#[0, 0, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4]
# def sample(n,fre_list):
#     i=0
#     res=[]
#     prob=[k**0.75 for k in fre_list]
#     sub_prob=prob[i]/sum(prob)
#     for num in range(n): ##抽取第NUM个时，应该抽取谁？
#         res.append(i)
#         if num>sub_prob*n: ##对于第i个值及前面的值应该抽取sub_prob*n次，但是我要抽取的次数比能抽取的次数大了，说明现在能抽取次数不够了，应该在次扩展i
#             i+=1
#             sub_prob+=(prob[i]/sum(prob))
#     return res
# cnt = [1, 2, 3, 100, 15]
# print(sample(34, cnt))







# board=[['.']*n for _ in range(n)]
# print(board)
# board[0][1]='Q'
# print(board)
# a=[]
# for i in board:
# #     a.append(''.join(i))
# # print(a)
# t='adaw'
# dicst={}
# for i in t:
#     dicst[i]=dicst.get(i,0)+1
# print(dicst)
# a="+2147483647"
# print(a[2],type(a[2]))
#
# str=''
# pattern=''
# if not pattern:
#     print(not str)
# dic={}
# num=[1,2,3,2]
# for i in range(len(num)):
#     dic[num[i]]=i
# print(dic)
# s='0030'
# s=list(s)
# j=2
# s[j]=str(int(s[j])-1)
# print(''.join(s))
# str='100'
# for i in range(len(str)):
#     val=ord(str[i])-ord('0')
#     print(val)
#     if 0<=val<=9:
#         continue
#     else:
#         print('False')
# left=0
# piles=0
# right=piles
# if left==piles:
#     piles+=1
# print(left)

# import sys
# for line in sys.stdin:
#     print(line,type(line))
# # import sys
# # for line in sys.stdin:
# #     a=line.split()
# #     print(int(a[0])+int(a[1]))
# # import sys
# # a=int(sys.stdin.readline().strip())
# # # for i in range(a):
# # # #     a,b=sys.stdin.readline().strip().split()
# # # #     print(int(a)+int(b))
# height=[4, 3, 2, 8,1, 3, 0, 5, 0, 1]
# left=0
# right=0
# res={}
# for i in range(1,len(height)-1):
#     left=max(height[:i])
#     right=max(height[i+1:])
#     val=min(left,right)-height[i]
#     if val>0:
#         res[(left,right)]=res.get((left,right),0)+val
# result=[]
# for j in res:
#     result.append(res[j])
# if result!=[]:
#     print( min(result))
# else:
#     print( 0)
# # result=[]
# for j in res:
#     sum = 0
#     for k in res[j]:
#         if k > 0:
#             sum += k
#     if sum>0:
#         result.append(sum)
# print(result)
# if result!=[]:
#     print(min(result))
# else:
#     print(0)
# a={(4, 8): 3, (8, 5): 11, (8, 1): 1}
# print(min(a))
# matchPairList=[[0,103],[1,103],[1,104],[2,104],[2,105],[2,106],[3,103]]
# peop=[]
# gang=[]
# for i in range(len(matchPairList)):
#     peop.append(matchPairList[i][0])
#     gang.append(matchPairList[i][1])
# gang=list(set(gang))
# print(len(gang)-1)
# a=[(1,2),(3,4)]
# a[0][0]=6
# print(a)
# def ends(x,y):
#     if x[1]>y[1]:
#         return  y,x
#     else:
#         return x,y
# a=[ [1,2], [2,3], [3,4], [1,3] ]
# a1=a.sort(ends)
# print(a1)

# a=[ [1,2], [1,3], [3,4], [1,3] ]
# a=sorted(a,key=lambda d:d[1])
# print(a)
# prices=[1,2,3,4,5]
# dp=[[[0]*2 for _ in range(3)] for j in range(len(prices)+1)]
# print(dp)
#
# for k in range(len(prices)+1):
#     dp[k][0][0]=0
#     dp[k][0][1]=-float('INF')
# print(dp)
# prices=[2,4,1]
# k=2
# dp=[[[0]*2 for _ in range(k+1)] for _ in range(len(prices)+1)]
# for i in range(len(dp[0])):
#     dp[0][i][0]=0
#     dp[0][i][1]=-float('INF')
# for j in range(1,len(prices)+1):
#     dp[j][0][0]=0
#     dp[j][0][1]=-float('INF')
# print(dp)
# for m in range(1,len(prices)+1):
#     for n in range(1,k+1):
#         dp[m][n][0]=max(dp[m-1][n][0],dp[m-1][n][1]+prices[i-1])
#         dp[m][n][1]=max(dp[m-1][n][1],dp[m-1][n-1][0]-prices[i-1])
#         print(dp)
# print(dp[len(prices)][k][0])
# import sys
# # zhan = sys.stdin.readline().strip()
# # print(type(zhan))
# qujian=[[0,5],[0,9],[6,10]]
# res=[]
# result=[]
# ass=[]
# for i in range(len(qujian)):
#     if qujian[i] not in ass:
#         end=qujian[i][1]
#         res.append(qujian[i])
#         for j in range(i+1,len(qujian)):
#             if qujian[j][0]>end:
#                 res.append(qujian[j])
#                 ass.append(qujian[j])
#                 end=qujian[j][1]
#         result.append(res)
#         res=[]
#     else:
#         continue
# print(res)
# print(result)
# end=[]
# for j in range(len(result)):
#     for k in range(len(result[j])):
#         end.append([j+1]+result[j][k])
# print(end)
#
#
# import sys
# zhan = int(sys.stdin.readline().strip())
# wei=int(sys.stdin.readline().strip())
# qujian=sys.stdin.readline().strip()
# qujian=eval(qujian)
# qujian=sorted(qujian,key=lambda d:d[0])
# res=[]
# result=[]
# ass=[]
# for i in range(len(qujian)):
#     if qujian[i] not in ass:
#         end=qujian[i][1]
#         res.append(qujian[i])
#         ass.append(qujian[i])
#         for j in range(i+1,len(qujian)):
#             if qujian[j][0]>=end:
#                 res.append(qujian[j])
#                 ass.append(qujian[j])
#                 end=qujian[j][1]
#         result.append(res)
#         res=[]
#     else:
#         continue
# if len(result)>wei:
#     result=result[:wei-1]
# end=[]
# for j in range(len(result)):
#     for k in range(len(result[j])):
#         end.append([j+1]+result[j][k])
# # print(end)
# pre=[0,0,0,0,0]
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         pre[j]=pre[j]+1 if matrix[i][j]=="1" else 0
#     print(pre)
#
# a=[1,2]
# for i in range(len(a)):
#     print(i)
# if i==len(a):
#     print('shi')

# def nextGreaterElements( nums):
#     lens = len(nums)
#     nums = nums + nums
#     res = []
#     stack = []
#     for i in range(len(nums) - 1, -1, -1):
#         if stack != [] and stack[-1] <= nums[i]:
#             stack.pop(-1)
#         res.append(stack[-1] if stack != [] else -1)
#         stack.append(nums[i])
#     res = res[::-1]
#     print(res)
#     return res[:lens]
# num=[1,2,1]
# aa=nextGreaterElements(num)
# print(aa)

# res=[]  ##可变对象
# def sub( nums, start, track):
#     print("1",track)
#     res.append(track[:])
#     print("2",track)
#     print("3",res)
#     for i in range(start, len(nums)):
#         track.append(nums[i])  ##track也是可变对象，创建可变对象会导致地址发生变化
#         sub(nums, i + 1, track)
#         track.pop(-1)
# sub([1,2,3],0,[])
# print(res)

#
# a=[1]
# print(id(a))
# a.append(3)
# print(id(a))
# a=[1,2,3]
# print(id(a))
# b=a
# print(id(b))
# c=a[:]
# print(id(c))

# l1=[1,2,3]
# l2=[1,2,3]
# a=1
# b=11
# print(id(l1))
# print(id(l2))
# print(id(a))
# print(id(b))
# a=1
# print(id(a))
# def x(a):
#   print(id(a))
#   b=a
#   print(id(b))
# x(a)
# a=1
# print(id(a))
# def x(a):
#     print(id(a))
#     b=a
#     print(id(b))
#     a+=1
#     print(id(a))
#     print(id(b))
# # x(a)
# l=[1,2,3]
# # print(id(l))
# def a(x):
#   print(id(x))
#   x.pop()
#   # print(x)
#   print(id(x))
#   x+=[3]
#   # print(x)
#   print(id(x))
# a(l)
# a=[1,2]
# print(id(a))
# a+=[2]
# print(id(a))
# a=a+[2]
# print(id(a))
# a='dwd'
# a=a[:-1]
# # print(a)
# board=[['E','M']]
# c=0
# c+=board[0][1]=='M'
# c+=board[0][0]=='E'
# print(c)

# def merge(intervals):
#     intervals.sort(key=lambda d: d[0])
#     res = []
#     res.append(intervals[0])
#     for i in range(1, len(intervals)):
#         cur = intervals[i]
#         last = res[-1]
#         print("1",res)
#         if cur[0] <= last[1]:
#             last[1] = max(cur[1], last[1])
#             print("2",res)
#         else:
#             res.append(cur)
#             print("3",res)
#     return res
# merge([[1,3],[2,6],[8,10],[15,18]])

# a=[[6,2],[2,5],[2,2],[5,4],[6,7],[6,4],[2,3]]
# a.sort()
# # print(a)
# a=[1,2,3]
# print(max(a))
# a=[[4,5],[4,6],[6,7],[2,3],[1,1]]
# def comp(a,b):
#     if a[0]==b[0]:
#         if a[1]<b[1]:
#             return [b,a]
#         else:
#             return [a,b]
#     else:
#
#
# a.sort(key=comp)
# print(a)
# a.sort()
# aa=[i[1] for i in a]
# # print(aa)
# def LIS( assis):
#     dp = [1] * len(assis)
#     for i in range(1, len(assis)):
#         for j in range(i - 1, -1, -1):
#             if assis[j] < assis[i]:
#                 dp[i] = max(dp[i],dp[j] + 1)
#     print(dp)
#
#     return max(dp)
# print(LIS(aa))
# print(11//2)
# s1='qweq'
# s2='we'
# s3='e'
# res=max(len(s1),len(s2),len(s3))
# print(res)
# a='efwef'
# # print(a[2:5])
# def findErrorNums(nums):
#     dicss = {}
#     for i in range(len(nums)):
#         dicss[nums[i]] = dicss.get(nums[i], 0) + 1
#     return dicss
# print(findErrorNums([1,2,2,4]))
# s=['dwqw','wee2312',':wj32',',efj','2312','  ']
# for i in range(len(s)):
#     if s[i].isalnum():
#         print("1",s[i])
#     else:
#         print("2",s[i])
# import random
# a=random.randint(0,2)
# aa=1
# print(id(aa))
# bb=aa
# print(id(bb))
# a='I speak Chicken Latin'
# # print(a.split())
# # i=2
# # a=['a' for j in range(i)]
# # print(''.join(a))
# # a='dwdwdwe'
# # print(a[1:]+a[0])
# import sys
# yuanyin=['a','e','i','o','u','A','E','I','O','U']
# strs=sys.stdin.readline().strip()
# lists=strs.split()
# result=[]
# for i in range(len(lists)):
#     s=lists[i]
#     res=''
#     if s[0] not in yuanyin:
#         s=lists[i][1:]+lists[i][0]
#     res+=(s+'pdd')
#     a=['a' for j in range(i+1)]
#     res+=''.join(a)
# #     result.append(res)
# # print(' '.join(result))
#
# #Ipdda peakspddaa hickenCpddaaa atinLpddaaaa
# import sys
# # N = int(sys.stdin.readline().strip())
# strs = list(sys.stdin.readline().strip())
# dicss = {}
# for i in range(len(strs)):
#     dicss[strs[i]] = dicss.get(strs[i], 0) + 1
# print(dicss)
# dic1={}
# #{'3': 3, 'A': 3, 'J': 1, 'Q': 1, 'K': 4}
# for k in dicss:
#     dic1[dicss[k]]=dic1.get(dicss[k],0)+1
# print(dic1)
# a={1:2,3:3}
# if 3 in a:
#     print("shi")

# import sys
# N=int(sys.stdin.readline().strip())
# strs=list(sys.stdin.readline().strip())
# dicss={}
# for i in range(len(strs)):
#     dicss[strs[i]]=dicss.get(strs[i],0)+1
# dic1={}
# for k in dicss:
#     dic1[dicss[k]]=dic1.get(dicss[k],0)+1
# count=0
# for k in dic1:
#     if k==4:
#         count+=dic1[4]
#     if k==2:
#         count+=dic1[2]
#     if k==3:
#         count+=dic1[3]
#     if k==1 and 3 in dic1:
#         a=dic1[1]-dic1[3]
#         if a>0:
#             count+=a
#         else:
#             count+=0
#     if k==1 and 3 not in dic1:
#         count+=dic1[1]
# print(count)
# import sys
# # a1=sys.stdin.readline().strip()
# # n,k=a1.split()
# # n=int(n)
# # k=int(k)
# # lists=sys.stdin.readline().strip()
# # lists=lists.split()
# # print(lists)
# # a=['1','2','7','3','6','9','233','322']
# # # a.sort()
# # # print(a)
#
# import sys
#
# a1 = sys.stdin.readline().strip()
# n, k = a1.split()
# n = int(n)
# k = int(k)
# lists = sys.stdin.readline().strip()
# lists = lists.split()
# list1 = []
# for i in range(len(lists)):
#     list1.append(int(lists[i]))
#
# res = 0
# s = 0
# e = s + k
# while e<=n:
#     val = sorted(list1[s:e])
#     print("val",val)
#     res += val[(k - 1) // 2]
#     s += 1
#     e = s + k
# print(res)

# import sys
# a1=sys.stdin.readline().strip()
# lists=list(a1.split())
# print(lists)
# # n=int(lists[0])
# # m=int(lists[1])
# # x0=int(lists[2])
# # y0=int(lists[3])
# # x1=int(lists[4])
# # y1=int(lists[5])
# print(-1)
# import sys
# N=int(sys.stdin.readline().strip())
# strs=list(sys.stdin.readline().strip())
# dicss={}
# for i in range(len(strs)):
#     dicss[strs[i]]=dicss.get(strs[i],0)+1
# print(dicss)
# dic1={}
# for k in dicss:
#     dic1[dicss[k]]=dic1.get(dicss[k],0)+1
# print(dic1)
# count=0
# for k in dic1:
#     if k==4:
#         count+=dic1[4]
#     if k==2:
#         count+=dic1[2]
#     if k==3:
#         count+=dic1[3]
#     if k==1 and 3 in dic1:
#         a=dic1[1]-dic1[3]
#         if a>0:
#             count+=a
#         else:
#             count+=0
#     if k==1 and 3 not in dic1:
#         count+=dic1[1]
# print(count)
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Codec:
#     def __init__(self):
#         self.res = ''
#
#     def serialize(self, root):
#         if not root:
#             self.res += '#!'
#             return
#         self.serialize(root.left)
#         self.serialize(root.right)
#         self.res += (str(root.val) + '!')
#
#     def deserialize(self, data):
#         res = self.res.split('!')
#         res.pop(-1)
#         if len(res) == 1:
#             return None
#
#         def pre_order():
#             if len(res) == 0:
#                 return None
#             val = res.pop(-1)
#             if val == '#':
#                 return None
#             treenode = TreeNode(int(val))
#             treenode.right = pre_order()
#             treenode.left = pre_order()
#             return treenode
#
#         return pre_order()
# def moveZeroes(nums):
# #     slow = 0
# #     fast = 0
# #     while fast < len(nums):
# #         if nums[fast] != 0:
# #             nums[slow] = nums[fast]
# #             slow += 1
# #         fast += 1
# #     lens = len(nums) - slow
# #     return nums[:slow] + ([0] * lens)
# # # print(moveZeroes([0,1,0,3,12]))
# def slidingPuzzle( board):
#     start = ''
#     targrt = '123450'
#     for val in board:
#         start += str(val)
#
#     queue = []
#     visit = set()
#     queue.append(start)
#     visit.add(start)
#
#     nebors = [{1, 3}, {0, 4, 2}, {1, 5}, {0, 4}, {3, 1, 5}, {4, 2}]
#     step = 0
#
#     while queue:
#         sz = len(queue)
#         for i in range(sz):
#             cur = queue.pop(0)
#             print(cur)
#             if cur == targrt:
#                 return step
#             indx = cur.index('0')
#             print(indx)
#             for j in nebors[indx]:
#                 cur1 = cur
#                 cur1[indx], cur1[j] = cur1[j], cur1[indx]
#                 if cur not in visit:
#                     visit.add(cur)
#                     queue.append(cur)
#         step += 1
#     return -1
# print(slidingPuzzle([[1,2,3],[4,0,5]]))
# def findKthLargest(self, nums, k):
#     new_nums = self.fast_rank(nums)
#     return new_nums[len(new_nums) - k]

#
# def fast_rank( nums):
#     if len(nums) <= 1:
#         return nums
#     a = nums[0]
#     left = fast_rank([nums[i]  for i in range(1, len(nums)) if nums[i]<=a])
#     right = fast_rank([nums[j] for j in range(1, len(nums)) if nums[j]>a])
#     return left + [a] + right
# print(fast_rank([1,4,2,3,7,5,2]))
# from heapq import *
# def findKthLargest( nums, k):
#     res = []
#     for i in range(len(nums)):
#         heappush(res, nums[i])
#         if len(res) > k:
#             res.pop(0)
#     print(res)
#     return res[0]
# print(findKthLargest([3,2,1,5,6,4],2))
# import random
# def shuffle(nums):
#     for i in range(len(nums)):
#         a = i + random.randint(0, len(nums) - i - 1)
#         nums[i], nums[a] = nums[a], nums[i]
#     return nums
# print(shuffle([4,5,3,7,2,5]))
# from sys import stdin
# nums=int(stdin.readline().strip())
# for line in range(nums):
#     val=stdin.readline().strip()
#     lst=val.split()
#     lst=sorted(list(map(int,lst)))
#     print(lst,type(lst[0]))
# import collections
# m = collections.defaultdict(list)
# print(m)
# dics={5:0,3:4,1:2}
# dict=sorted(dics.items(),key=lambda d:d[1])
# print(dict[::-1])
# strs=["flower","flow","flight"]
# strs=sorted(strs,key=lambda d:len(d))
# min_len=strs[0]
# for i in range(len(min_len)):
#     print([not s.startswith(min_len[0:i]) for s in strs])
#     print(any([not s.startswith(min_len[0:i ]) for s in strs]))

# # from heapq import *
# a='dfwefggfjwf'
# b='fgg'
# print(a.index(b))
#
# def merge( nums1, m, nums2, n):
# #     nums = nums1[:m] + nums2
# #     nums = sorted(nums)
# #     return nums
# # print(merge([1,2,3,0,0,0],3,[2,5,6],3))
# dic={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
# result=[]
# def backtrack( digits, indx, res):
#     if indx == len(digits[0]):
#         result.append(res[:])
#         return
#     strs = dic[digits[0][indx]]
#     for i in range(len(strs)):
#         res = res + (strs[i])
#         backtrack(digits, indx + 1, res[:])
#         res = list(res)
#         res.pop(-1)
#         res = ''.join(res)
# backtrack(['23'],0,'')
# print(result)
# digits='23'
# # dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
# # queue=[]
# # queue.extend(list(dic[digits[0]]))
# # print(queue)
# a=[[1,2,3],[4,5,6],[1,2,3]]
# print(list(set(a)))
# def threeSum(nums):
#     n = len(nums)
#     if (not nums or n < 3):
#         return []
#     nums.sort()
#     res = []
#     for i in range(n):
#         if (nums[i] > 0):
#             return res
#         if (i > 0 and nums[i] == nums[i - 1]):
#             continue
#         L = i + 1
#         R = n - 1
#         while (L < R):
#             if (nums[i] + nums[L] + nums[R] == 0):
#                 res.append([nums[i], nums[L], nums[R]])
#                 while (L < R and nums[L] == nums[L + 1]):
#                     L = L + 1
#                 while (L < R and nums[R] == nums[R - 1]):
#                     R = R - 1
#                 L = L + 1
#                 R = R - 1
#             elif (nums[i] + nums[L] + nums[R] > 0):
#                 R = R - 1
#             else:
#                 L = L + 1
#     return res
# print(threeSum([-1,0,1,2,-1,-4]))
# class Solution(object):
#     def threeSum(self, nums):
#         if len(nums)<3:
#             return []
#         nums.sort()
#         return self.nsum(nums,0,3,0)
#     def nsum(self,nums,target,n,start):
#         res=[]
#         if n<2 or len(nums)<n:
#             return res
#         elif n==2:
#             l=start
#             r=len(nums)-1
#             while l<r:
#                 if nums[l]+nums[r]==target:
#                     res.append([nums[l],nums[r]])
#                     while l<r and nums[l]==nums[l+1]:
#                         l+=1
#                     while l<r and nums[r]==nums[r-1]:
#                         r-=1
#                     l+=1
#                     r-=1
#                 elif nums[l]+nums[r]<target:
#                     l+=1
#                 else:
#                     r-=1
#         else:
#             for i in range(start,len(nums)):
#                 if i>start and nums[i]==nums[i-1]:
#                     continue
#                 ress=self.nsum(nums,target-nums[i],n-1,i+1)
#                 if ress!=[]:
#                     for lst in ress:
#                         res.append([nums[i]]+lst)
#         return res
# def myAtoi( s):
#     s = s.strip()
#     new_s = list(s)
#     flag = 1
#     res = 0
#     for i in range(len(new_s)):
#         if new_s[i] in ['+', '-']:
#             if i == 0 and new_s[i] == '-':
#                 flag = -1
#         elif 0 <= ord(new_s[i]) - ord('0') <= 9:
#             res = (res * 10) + int(new_s[i])
#         else:
#             break
#     return  res*flag
# print(myAtoi('43'))
# a=''
# new_a=a.split()
# # print(new_a[-1])
# lst=[1,3,4,0,0,0,0,0,0,1]
# dp=[0]*(len(lst))
# dp[0]=1
# for i in range(1,len(lst)):
#     if i<len(lst) and lst[i] != 0:
#         for j in range(0,i):
#             if int(lst[j])>=(i-j):
#                 dp[i]+=dp[j]
# print(dp)






# from sys import stdin
# a=int(stdin.readline().strip())
# res=[]
# for i in range(a):
#     a=stdin.readline().strip()
#     b=a.split()
#     res.append([int(b[0]),int(b[1])])
# print(res)
# from sys import stdin
# a=int(stdin.readline().strip())
# res=[]
# for i in range(a):
#     a=stdin.readline().strip()
#     b=a.split()
#     res.append([int(b[0]),int(b[1])])
#
# res.sort(key=lambda d:(d[0],-d[1]))
# new_res=[]
# for a1,a2 in res:
#     new_res.append(a2)
#
# def sub(res):
#     piles=0
#     n=len(res)
#     top=[0]*n
#     for i in range(0,n):
#         po=res[i]
#         left=0
#         right=piles
#         while left<right:
#             mid=(left+right)//2
#             if top[mid]>=po:
#                 right=mid
#             else:
#                 left=mid+1
#         if left==piles:
#             piles+=1
#         top[left]=po
#     return piles
# # print(sub(res))
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# ass=[]
# for i in range(len(matrix[0])):
#     a=[]
#     for j in range(len(matrix)):
#         a.append(matrix[j][i])
#     ass.append(a[::-1])
# print(ass)
# a = "11"
# b='1'
# a=list(a)
# b=list(b)
# len_a=len(a)
# len_b=len(b)
# if len_a<len_b:
#     a=['0']*(len_b-len_a)+a
# elif len_a>len_b:
#     b=['0']*(len_a-len_b)+b
# # print(a,b)
# a=['1','2']
# # numbers = map(int, numbers)
# a=list(map(int,a))
# print(a)
# a='10010'
# b='1110'
# x, y = int(a, 2), int(b, 2)
# while y:
#     answer = x ^ y
#     carry = (x & y) << 1
#     x, y = answer, carry
#     print(bin(x)[2:],bin(y)[2:])

# dic={1:'I',4:'IV',5:'V'}
# print(list(dic.keys()))
# res=''
# hashmap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
#            4: 'IV', 1: 'I'}
# print(hashmap.keys())
# print(hashmap.values())
# nums = [3,2,1]
# def reverse( nums, start, end):
#     while start < end:
#         nums[start], nums[end] = nums[end], nums[start]
#         start += 1
#         end -= 1
# for i in range(len(nums)-1,0,-1):
#     if nums[i-1]<nums[i]:
#         for j in range(len(nums)-1,i-1,-1):
#             if nums[j]>nums[i-1]:
#                 nums[j],nums[i-1]=nums[i-1],nums[j]
#                 break
#         reverse(nums,i,len(nums)-1)
#         print(nums)
#         break
# print(i)
# a={1:'2',2:'3',3:'5'}
# b={2:'3',3:'5',1:'2'}
# print(a==b)
# def minimumTotal( triangle):
# #     if len(triangle) == 0 or len(triangle[0]) == 0:
# #         return 0
# #     dp = [0] * len(triangle)  ##表示从0到i行的最小值
# #     dp[0]=triangle[0][0]
# #     start = 0
# #     for i in range(1, len(triangle)):
# #         if start + 1 < len(triangle) and triangle[i][start] <= triangle[i][start + 1]:
# #             dp[i] = dp[i - 1] + triangle[i][start]
# #             start = start
# #         elif start + 1 < len(triangle) and triangle[i][start] >triangle[i][start + 1]:
# #             dp[i] = dp[i - 1] + triangle[i][start + 1]
# #             start = start + 1
# #         print(start)
# #     return dp[-1]
# # triangle = [[-1],[2,3],[1,-1,-3]]
# # # print(minimumTotal(triangle))
# nums = [-1,-100,3,99]
# # print(nums[-2:] + nums[:-2])
# nums = [1,2,3,4,5,6]
# k = 3
# count=0
# n=len(nums)
# for i in range(n):
#     print("i",i)
#     tmp=nums[i]
#     x1=(i+k)%n
#     while i!=x1:
#         nums[x1],tmp=tmp,nums[x1]
#         x1=(x1+k)%n
#         count+=1
#
#     nums[x1],tmp=tmp,nums[x1]
#     count+=1
#
#     if count==n:
#
#         break
# print(nums)
# s="226"
# dp=[0]*len(s)
# dp[0]=1
# for i in range(1,len(s)):
#     if s[i]!='0':
#         if 0 <= i - 1 and i + 1 < len(s) and s[i + 1] != '0' and  s[i - 1]+s[i] <= '26':
#             dp[i] = dp[i - 1] + 1
#             print("1",i)
#         elif 0 <= i - 1 and i + 1 >= len(s) and s[i - 1]+s[i] <= '26':
#             dp[i] = dp[i - 1] + 1
#             print("2",i)
#         else:
#             dp[i] = dp[i - 1]
#             print("3",i)
#     else:
#         dp[i]=dp[i-1]
# print(dp)
# n=3
# res=[0]*(n+1)
# for i in range(n+1):
#     i=i
#     count=0
#     while i!=0:
#         i=i&(i-1)
#         count+=1
#     res[i]=count
# print(res)
# def longestPalindrome( s):
#     dic = {}
#     for i in range(len(s)):
#         dic[s[i]] = dic.get(s[i], 0) + 1
#     res = 0
#     max_odd = 0
#     new_s = list(set(list(s)))
#     for j in range(len(new_s)):
#         if dic[new_s[j]] % 2 == 0:
#             res += dic[new_s[j]]
#         else:
#             max_odd = max(max_odd, dic[new_s[j]])
#     return res + max_odd
# print(longestPalindrome("abcCccdd"))
# a={'1':0,'2':0}
# print(a.items())
# print(a.keys())
# # print(a.values())
# s=' f wf '
# a1=s.strip()
# print(s)
# print(a1)
# def firstMissingPositive( nums):
#     n = len(nums)
#     for i in range(len(nums)):
#         if nums[i] <= 0:
#             nums[i] = n + 1
#
#     for j in range(len(nums)):
#         print("j",j)
#         if 1 <= abs(nums[j])<= n:
#             indx=abs(nums[j])-1
#             if nums[indx]>0:
#                 nums[indx]=(-nums[indx])
#
#     for k in range(len(nums)):
#         if nums[k] > 0:
#             return k + 1
#     return n + 1
# print(firstMissingPositive([3,4,-1,1]))
# dic={'1':1,'3':4,'2':2}
# a=list(dic.items())
# a.sort(key=lambda k:-k[1])
# print(a)







# from sys import stdin
# a=stdin.readline().strip()
# lst=a.split(' ')
# counts=0
# for i in range(len(lst)):
#     if int(lst[i])%7==0 or '7' in lst[i]:
#         counts+=1
# print(counts)
# from sys import stdin
# total_weight=int(stdin.readline().strip())
# a=stdin.readline().strip()
# weights=a.split(',')
# b=stdin.readline().strip()
# values=b.split(',')
# n=len(values)
# dp=[[0]*(total_weight+1) for _ in range(n+1)]
# for i in range(1,n+1):
# #     for j in range(1,total_weight+1):
# #         if j-int(weights[i-1])<0:
# #             dp[i][j]=dp[i-1][j]
# #         else:
# #             dp[i][j]=max(dp[i-1][j-int(weights[i-1])]+int(values[i-1]),dp[i-1][j])
# # print(dp[n][total_weight])
#
# from sys import stdin
# total_weight=int(stdin.readline().strip())
# a=stdin.readline().strip()
# weights=a.split(',')
# weights=list(map(int,weights))
# b=stdin.readline().strip()
# values=b.split(',')
# values=list(map(int,values))
# n=len(values)
# dp=[[0]*(total_weight+1) for _ in range(n+1)]
# for i in range(1,n+1):
#     for j in range(1,total_weight+1):
#         if j-weights[i-1]<0:
#             dp[i][j]=dp[i-1][j]
#         else:
# #             dp[i][j]=max(dp[i-1][j-weights[i-1]]+values[i-1],dp[i-1][j])
# # print(dp[n][total_weight])
#
# # from sys import stdin
# # a=stdin.readline().strip()
# # nodes=a.split(',')
# # b=stdin.readline().strip()
# # yilai=b.split(';')
# # print(nodes,yilai)
# # a=[5,2,3]
# # for i in range(len(a)):
# #     a[i]=1
# #     if i!=0 and a[i-1]==1:
# #         print(i)
# # dic={'1':(1,2),'3':(2,3)}
# # res=0
# # for val in dic:
# #     res=max(res,dic[val][0]+dic[val][1])
# #     print(res)
# # a='dwdqwfweaa'
# # print(a.count('w'))
# # a=[[1,2],[3,4]]
# # print(a[-1])
# # a=[[1,1,2],[1,2,1],[1,1,2],[1,2,1],[2,1,1],[2,1,1]]
# # dic = list(set([tuple(t) for t in a]))
# # dic = [list(v) for v in dic]
# # print(dic)
# def __init__(self):
#     self.counts = -1
#
# def orangesRotting(self, grid):
#     used = [[False] * len(grid[0]) for _ in range(len(grid))]
#     zero = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] != 1:
#                 zero += 1
#             if grid[i][j] == 2 and used[i][j] == False:
#                 self.bfs(grid, used, i, j)
#     if zero == (len(grid) * len(grid[0])):
#         return 0
#
#     for m in range(len(grid)):
#         for n in range(len(grid[0])):
#             if grid[m][n] == 1:
#                 return -1
#     return self.counts
#
#
# def bfs(self, grid, used, i, j):
#     queue = [[(i, j)]]
#     while queue:
#         node = queue.pop(0)
#         assis = []
#         for a, b in node:
#             used[a][b] = True
#             for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
#                 x1 = a + x
#                 y1 = b + y
#                 if (x1, y1) not in assis:
#                     if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]) and used[x1][y1] == False and grid[x1][y1] == 1:
#                         assis.append((x1, y1))
#                         grid[x1][y1] = 2
# #         self.counts += 1
# #         if assis != []:
# #             queue.append(assis)
# #
# # grid=[[2,1,1],[1,1,0],[0,1,1]]
# # zero=0
# # for i in range(len(grid)):
# #     for j in range(len(grid[0])):
# #         if grid[i][j]!=1:
# #             zero+=1
# # print(zero)
# # print(len(grid)*len(grid[0]))
# # if zero==(len(grid)*len(grid[0])):
# #     print('1')
# nums=[-1,2,1,-4]
# nums.sort()
# print(nums)
# target=1
# l=0
# r=len(nums)-1
# mins=float('inf')
# pos=[0,0]
# while l<r:
#     sums=nums[l]+nums[r]
#     if target-sums<mins:
#         mins=target-sums
#         pos=[l,r]
#         r-=1
#     else:
#         l+=1
# print(pos)
# new_nums=nums[:pos[0]]+nums[pos[0]+1:pos[1]]+nums[pos[1]+1:]
# # print(new_nums)
# a=[5,3,4,1,2,4]
# a.sort(key=lambda x:-x)
# print(a)



#lst=['a','b','c']
# def reverse(lst):
#     if len(lst)<=1:
#         return lst
#     left=0
#     right=len(lst)-1
#     while left<right:
#         lst[left],lst[right]=lst[right],lst[left]
#         left+=1
#         right-=1
#     return lst
# # # print(reverse(['a','b','c','d']))
# # a=[1,2,33]
# # print(a.pop())
#
# def decodeString(s):
#     value = 0
#     strs = ''
#     stack = []
#     i = 0
#     while i < len(s):
#         print(i)
#         if '0' <= s[i] <= '9':
#             value = value * 10 + int(s[i])
#         elif s[i] == '[':
#             stack.append([value, strs])
#             value = 0
#             strs = ''
#         elif s[i] == ']':
#             v1, s1 = stack.pop(-1)
#             strs = s1 + v1 * strs
#         else:
# #             strs += s[i]
# #         i += 1
# #     return strs
# # print(decodeString("3[a]2[bc]"))
# # a={'2':[1,2,3],'3':[4,5,6]}
# # print(list(a.values()))
# def wordPattern(pattern, s):
#     dic = {}
#     for i in range(len(pattern)):
#         if pattern[i] not in dic:
#             dic[pattern[i]] = []
#         dic[pattern[i]].append(i)
#     print(dic)
#     lst = list(dic.values())
#     # print(lst)
#     s=s.split()
#     for k in range(len(lst)):
#         tmp = s[lst[k][0]]
#         print(tmp)
#         for j in range(len(lst[k])):
#             if s[lst[k][j]] != tmp:
# #                 return False
# #     return True
# # print(wordPattern("abba","dog dog dog dog"))
# # a=[[1,2],[3,4]]
# # b=[[1,2],[3,4]]
# # print(a==b)
# def wordPattern( pattern, s):
#     dic1 = {}
#     for i in range(len(pattern)):
#         if pattern[i] not in dic1:
#             dic1[pattern[i]] = []
#         dic1[pattern[i]].append(i)
#
#     dic2 = {}
#     s=s.split()
#     for j in range(len(s)):
#         if s[j] not in dic2:
#             dic2[s[j]] = []
#         dic2[s[j]].append(j)
#
#     lst1 = list(dic1.values())
#     lst2 = list(dic2.values())
#     print(lst1,lst2,lst1==lst2)
# wordPattern("abc","b c a")
# a=[1,2,3]
# b=[1,2]
# print(a-b)
# a=['']*3
# # print(a)
# a,b=divmod(2,3)
# print(a,b)
# def addStrings( num1, num2):
#     len1 = len(num1)
#     len2 = len(num2)
#
# #     if len1 < len2:
# #         num1 = '0' * (len2 - len1) + num1
# #     else:
# #         num2 = '0' * (len1 - len2) + num2
# #
# #     res = []
# #     jinwei = 0
# #     for i in range(len(num1) - 1, -1, -1):
# #         jinwei, val = divmod(int(num1[i]) + int(num2[i]) + jinwei, 10)
# #         res.append(val)
# #     if jinwei == 1:
# #         res.append(1)
# #     return ''.join(res[::-1])
# # # print(addStrings('12','39'))
# # res=['1','2']
# # res=res[::-1]
# # print(res)
# # print(''.join(res))
# def groupAnagrams(strs):
#     res = []
#     strs1 = strs[:]
#     while len(strs1) > 0:
#         print("yuanshi,xin",strs,strs1)
#         lst = sub(strs1[0], 0, [])
#         assis = []
#         for i in range(len(lst)):
#             if lst[i] in strs:
#                 assis.append(lst[i])
#                 del strs1[strs1.index(lst[i])]
#         res.append(assis)
#     return res
#
# def sub(s, pos, res):
#     if s=='':
#         return  ['']
#     new_s = list(s)
#     if pos == len(new_s):
#         res.append(s)
#         return
#     for i in range(pos, len(new_s)):
#         new_s[i], new_s[pos] = new_s[pos], new_s[i]
#         s = ''.join(new_s)
#         sub(s, pos + 1, res)
#         new_s[i], new_s[pos] = new_s[pos], new_s[i]
#     return res
# # print(sub('',0,[]))
# print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# # a=['1','2']
# # b=a
# # del b[0]
# # print(b,a)
# def groupAnagrams( strs):
#     res = []
#     strs1 = strs[:]
#     while len(strs1) > 0:
#         lst = sub(strs1[0], 0, [])
#         assis = []
#         for i in range(len(lst)):
#             if lst[i] in strs1:
#                 while lst[i] in strs1:
#                     assis.append(lst[i])
#                     del strs1[strs1.index(lst[i])]
#         res.append(assis)
#     return res
#
#
# def sub(s, pos, res):
#     if s == '':
#         return ['']
#     new_s = list(s)
#     if pos == len(new_s):
#         res.append(s)
#         return
#     for i in range(pos, len(new_s)):
#         new_s[i], new_s[pos] = new_s[pos], new_s[i]
#         s = ''.join(new_s)
#         sub(s, pos + 1, res)
#         new_s[i], new_s[pos] = new_s[pos], new_s[i]
#     return res
# print(groupAnagrams([["bdddddddddd","bbbbbbbbbbc"]]))
# a='fssf'
# b=sorted(a)
# print(b)
# def longestValidParentheses(s) :
#     stack = []
#     res = 0
#     for i in range(len(s)):
#         if not stack or s[i] == '(' or s[stack[-1]] == ')':
#             stack.append(i)
#         else:
#             stack.pop()
#             res = max(res, i - (stack[-1] if stack else - 1))
#             print(res)
#         print(stack)
#     return res
# print(longestValidParentheses('(())(()()()'))
# a=[1,3,4,2,2,2]
# res=0
# for val in a:
#     res^=val
# print(res)
# a='fsfsfwf'
# b=a.replace(a[0],'')
# print(b)

# import pandas as pd
# content=pd.read_excel(r'c:\Users\admin\Desktop\频次表.xlsx')
# bianhao=[]
# zh_name=[]
# en_name=[]
# jiancheng=[]
# freq=[]
# review=[]
# for i in range(len(content)):
#     with open(r'C:\Users\admin\Desktop\更新表.txt',encoding='utf-8') as f:
#         for j,eachline in enumerate(f):
#             if j!=0:
#                 a=eachline.split()
#                 if int(a[0])==int(content['编号'][i]):
#                     if len(a[1])>4:  ##以运营的结果为主，主要还需核实英文改如何定义长度
#                         review.append(1)
#                     else:
#                         review.append(0)
#                     bianhao.append(a[0])
#                     zh_name.append(content['中文名称'][i])
#                     en_name.append(content['英文名称'][i])
#                     jiancheng.append(a[1])
#                     freq.append(content['频次'][i])
#                     break
# bianhao=pd.DataFrame(bianhao,columns=['编号'])
# zh_name=pd.DataFrame(zh_name,columns=['中文名称'])
# en_name=pd.DataFrame(en_name,columns=['英文名称'])
# jiancheng=pd.DataFrame(jiancheng,columns=['简称'])
# freq=pd.DataFrame(freq,columns=['频次'])
# review=pd.DataFrame(review,columns=['是否需要核实'])
# b=pd.concat([bianhao,zh_name,en_name,jiancheng,freq,review],axis=1)
# b.to_csv(r'c:\Users\admin\Desktop\verify_brand_name.csv',encoding='utf-8',index=False)

# for i in range(len(word)):
#     if i%10000==0:
#         print(i)
#     group_data=data[data.zh_term==word[i]]
#     group_data = group_data.reset_index()
#     group_data = group_data.drop(columns='index')
#     group_data=group_data.sort_values(by=['cos_sim'],ascending=False)
#     group_data.to_csv(r'd:\法语处理\有or没有翻译筛选\candidate_zhfr_termpair_quchong_label_small_token_cos_jiancha.csv',mode='a',header=0,index=False)

#
# import pandas as pd
# data=pd.read_excel(r'c:\Users\admin\Desktop\实验.xlsx')
# word=['办公室','资本 市场']
# for i in range(len(word)):
#     group_data=data[data.zh_term==word[i]]
#     group_data=group_data.reset_index()
#     group_data=group_data.drop(columns='index')
#     group_data=group_data.sort_values(by='b',ascending=False)
#     group_data.to_csv(r'c:\Users\admin\Desktop\实验1.csv',index=False,header=0,mode='a')

# def chooses(dic,word):
#     dic1=dic
#     for i in range(len(word)):
#         if word[i] in dic1 and dic1[word[i]]!=0:
#             dic1[word[i]]-=1
#         else:
#             return 0
#     return len(word)
#
# ##将chars的情况存储在词典中，逐一判断
# def countCharacters(words, chars):
#     dic={}
#     for s in chars:
#         dic[s]=dic.get(s,0)+1
#     res=0
#     for k in range(len(words)):
#         res+=chooses(dic,words[k])
#     return res
# words = ["cat","bt","hat","tree"]
# chars = "atach"
# print(countCharacters(words,chars))
#
# def findShortestSubArray( nums):
#     dic = {}
#     for i in range(len(nums)):
#         if nums[i] not in dic:
#             dic[nums[i]] = []
#         dic[nums[i]].append(i)
#     print(dic)
#     val = dic[nums[0]]
#     lens = len(val)
#     res = len(nums)
#     for k in dic:
#         if len(dic[k]) >= lens:
#             val = dic[k]
#             lens = len(val)
#             res =min(res,val[-1]-val[0]+1)
#     return res
#
# print(findShortestSubArray([1,2,2,3,1,4,2]))
# a={1:2,3:4}
# print(a.values())

# import  numpy as np
# def numSquares( n):
#     if n == 0:
#         return 0
#     a = int(np.sqrt(n))
#     res = float('inf')
#     for i in range(a, 0, -1):
#         res = min(res, numSquares(n - i * i) + 1)
#     return res
# print(numSquares(12))
#
#
#
# class Solution(object):
#     def __init__(self):
#         self.res = float('inf')
#
#     def numSquares(self, n):
#         self.sub(n, 0)
#         return self.res
#
#     def sub(self, n, assis):
#         if assis >= self.res:
#             return float('inf')
#
#         if n == 0:
#             self.res = assis
#             return assis
#
#         a = int(np.sqrt(n))
#         res = float('inf')
#         for i in range(a, a // 2, -1):
#             res = min(res, self.sub(n - i * i, assis + 1))
#         print("1",res,assis)
#         return res
# a=Solution()
# print(a.sub(12,0))
import numpy as np
# def numSquares(n):
# #     dp = [0] + [float('inf')] * n
# #     rg = int(np.sqrt(n))
# #     for i in range(1, rg + 1):
# #         curr = i * i
# #         for j in range(curr, n + 1):
# #             dp[j] = min(dp[j], dp[j - curr] + 1)
# #     print(dp)
# #     return dp[n]
# # print(numSquares(12))
# def maxProduct( nums):
#     reverse_nums = nums[::-1]
#     for i in range(1, len(nums)):
#         nums[i] *= nums[i - 1] or 1
#         reverse_nums[i] *= reverse_nums[i - 1] or 1
#     print(nums,reverse_nums,nums + reverse_nums)
#     return max(nums + reverse_nums)
# print(maxProduct([3,-1,4]))
a=3
a*=0 or 1
print(a)
