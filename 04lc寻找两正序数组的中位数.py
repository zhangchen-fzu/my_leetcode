'''
#############################################################################################################
**题目04：（数组）
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
**示例：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
**条件：
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
**进阶：
你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
#############################################################################################################
'''

'''
暴力方法：
合并nums1和nums2之后排序，计算长度。
长度为奇数，中间的数为中位数；长度为偶数，中间两数的平均数为中位数
复杂度分析：
时间复杂度：排序函数sort,O((M+N)log(M+N))
空间复杂度：O(M+N)
'''
class Solution1(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums=nums1+nums2
        nums.sort()
        mid_len,nums_mod=divmod(len(nums),2)
        return nums[mid_len] if nums_mod else (nums[mid_len]+nums[mid_len-1])/2.0



'''
借助堆的有序性：
[1,2,3,4,5,6]将[1,2,3]放在大根堆中，[4,5,6]放在小根堆中，中位数即可通过取大根堆中第一个值及（或）小根堆中的第一个值快速得到
在向堆中存放值时须注意保持两个堆中元素个数的平衡。在python中默认堆是小根堆，大根堆可通过对元素值取负数实现
复杂度分析：
时间复杂度：O((M+N)log(M+N))
空间复杂度：nums的长度，O(M+N)
'''
from heapq import *
class Solution2(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums=nums1+nums2
        nums_len=len(nums)
        heapq1=[] #小堆
        heapq2=[] #负大堆
        for i in range(len(nums)):
            if len(heapq1)<len(heapq2):
                heappush(heapq2,-nums[i])
                heappush(heapq1,-heappop(heapq2))
            else:
                heappush(heapq1,nums[i])
                heappush(heapq2,-heappop(heapq1))
        if nums_len%2==0:
            return (heapq1[0]-heapq2[0])/2.0
        else:
            return heapq2[0]


'''
双指针方法：
两个指针分别控制两个数组的位置信息，不断移动指针并判断是否到达了中间位置
复杂度分析：
时间复杂度：O(M+N)
空间复杂度：O(M+N)
'''
class Solution3(object):
    def findMedianSortedArrays(self, nums1, nums2):
        i,j=0,0
        m,n=len(nums1),len(nums2)
        nums_div,nums_mod=divmod((m+n),2)
        res=[]
        while (i+j)<nums_div+1 and m>i and n>j:
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        if i==m: ##nums1执行完 剩下的从nums2中抽取值
            while (i+j)<nums_div+1:
                res.append(nums2[j])
                j+=1
        elif j==n: ##nums2执行完 剩下的从nums1中抽取值
            while (i+j)<nums_div+1:
                res.append(nums1[i])
                i+=1
        if nums_mod==0:
            return (res[-1]+res[-2])/2.0
        return res[-1]

'''
寻找第K小的数：
寻找中位数，就是在寻找第l//2小的元素及第l//2+1小的元素的均值（偶），或寻找l//2+1位置的元素（奇）
取两个数组中k//2位置元素进行比较，删除小的元素及其之前的元素（删除的这些元素一定不是第k小的元素，可参考证明：
（https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/di-k-xiao-shu-jie-fa-ni-zhen-de-dong-ma-by-geek-8m/），
改变k，改变数组的位置信息，继续寻找目标，直到k==1为止。注意边界信息，防止数组越界。
复杂度分析：
时间复杂度：初始折半，每轮折半，O(log(m+n))
空间复杂度：O(1)
'''
class Solution4(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m,n=len(nums1),len(nums2)
        nums_len=m+n
        mid_nums_len=nums_len//2
        def find_kth_num(k):
            i,j=0,0
            while k>0:
                if m==i:
                    return nums2[j+k-1]
                if n==j:
                    return nums1[i+k-1]
                if k==1:
                    return min(nums1[i],nums2[j])
                new_i=min(i+k//2-1,m-1) ##防止数组越界
                new_j=min(j+k//2-1,n-1)
                if nums1[new_i]<nums2[new_j]:
                    k=k-(new_i-i+1) ##改变k，继续去寻找第k小的元素
                    i=new_i+1
                else:
                    k=k-(new_j-j+1)
                    j=new_j+1
        if nums_len%2!=0:
            return find_kth_num(mid_nums_len+1)
        return (find_kth_num(mid_nums_len)+find_kth_num(mid_nums_len+1))/2.0

