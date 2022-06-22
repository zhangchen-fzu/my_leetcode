'''
#############################################################################################################
**题目88：（数组）
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。
**示例：
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
**条件：
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109
#############################################################################################################
'''

'''
非原地修改方法：
原地修改，想到双指针,若采用双指针从前到后比较两个数组中值的大小（原地），当需改变num1的位置时，需将num1后面的元素整体后移，操作过多
而采用新的空间存储排好序的元素时，可避免移动元素的操作
复杂度分析：
时间复杂度：O(M+N)
空间复杂度：O(M+N)
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        res=[]
        l=0
        r=0
        while m>l or n>r:
            if m==l:
                res.append(nums2[r])
                r+=1
            elif n==r:
                res.append(nums1[l])
                l+=1
            elif nums1[l]<nums2[r]:
                res.append(nums1[l])
                l+=1
            else:
                res.append(nums2[r])
                r+=1
        nums1[:]=res
        return nums1



'''
三指针方法： 
原地修改，想到双指针
若采用双指针从前到后比较两个数组中值的大小，当需改变num1的位置时，需将num1后面的元素整体后移，操作过多
但若从后到前比较两数组中值的大小，不断将大的值放在最后边，当需改变num1中元素位置时，直接移到合适位置即可
复杂度分析：
时间复杂度：O(M+N)
空间复杂度：O(1)
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i=m-1 #nums1
        j=n-1 #nums2
        k=m+n-1 #控制数值存放的位置
        while i>=0 or j>=0:
            if i==-1:
                nums1[:k+1]=nums2[:j+1]
                return nums1
            elif j==-1:
                return nums1
            if nums1[i]<=nums2[j]:
                nums1[k]=nums2[j]
                j-=1
            else:
                nums1[k]=nums1[i]
                i-=1
            k-=1
        return nums1