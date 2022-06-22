'''
#############################################################################################################
**题目215：（数组）
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
**示例：
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
**条件：
1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
#############################################################################################################
'''
'''
快排：
将第 k 个最大的元素改为寻找m-k位置的元素，判断已排好的元素位置与m-k位置的关系，去执行接下来的排序
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(logN)
'''
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        m = len(nums)
        if m < k:
            return False
        k, l, r = m - k, 0, m - 1
        while l <= r:
            p = self.quick_rank(nums, l, r)
            if p < k:  ##k位于已排好位置p的右边
                l = p + 1
            elif p > k: ##k位于已排好位置p的左边
                r = p - 1
            else:
                return nums[p]
        return -1
    def quick_rank(self,nums,start,end):
        if end == start:
            return start
        pivot_indx = random.randint(start,end)
        pivot = nums[pivot_indx]
        nums[start], nums[pivot_indx] = nums[pivot_indx], nums[start]
        l, r = start, end
        while l < r:
            while l < r and nums[r] >= pivot:
                r -= 1
            while l < r and nums[l] <= pivot:
                l += 1
            nums[l], nums[r] = nums[r], nums[l]
        nums[l], nums[start] = nums[start], nums[l]
        return l

def findKthLargest(nums, k):
    m = len(nums)
    if m < k:
        return False
    return quick_rank(nums, 0, m - 1,k)[m - k]
def quick_rank(nums, start, end,k):
    if end <= start:
        return nums
    pivot_indx = random.randint(start, end)
    pivot = nums[pivot_indx]
    nums[start], nums[pivot_indx] = nums[pivot_indx], nums[start]
    l, r = start, end
    while l < r:
        while l < r and nums[r] >= pivot:
            r -= 1
        while l < r and nums[l] <= pivot:
            l += 1
        nums[l], nums[r] = nums[r], nums[l]
    nums[l], nums[start] = nums[start], nums[l]
    if l<k:
        quick_rank(nums, start, l - 1,k)
    elif l<k:
        quick_rank(nums, l + 1, end,k)
    else:
        return nums

class Solution5(object):
    def findKthLargest(self, nums, k):
        m = len(nums)
        if m < k:
            return False
        k=m-k
        return self.quick_rank(nums, 0, m - 1, k)
    def quick_rank(self,nums, start, end,k):
        if end <= start:
            return nums
        pivot_indx = random.randint(start, end)
        pivot = nums[pivot_indx]
        nums[start], nums[pivot_indx] = nums[pivot_indx], nums[start]
        l, r = start, end
        while l < r:
            while l < r and nums[r] >= pivot:
                r -= 1
            while l < r and nums[l] <= pivot:
                l += 1
            nums[l], nums[r] = nums[r], nums[l]
        nums[l], nums[start] = nums[start], nums[l]
        if l>k:
            self.quick_rank(nums, start, l - 1,k)
        elif l<k:
            self.quick_rank(nums, l + 1, end,k)
        return nums
print(Solution5().findKthLargest([9,8,7,1,3,2,4,5,3], 5))




import collections
nums = [1,1,1,2,2,3]
val_fre_dic = collections.Counter(nums)
val_fre_lst = list(val_fre_dic.items())
m = len(val_fre_lst)

def fastrank(val_fre_lst, k, start, end):
    if start >= end:
        return val_fre_lst
    pivot = random.randint(start, end)
    val_fre_lst[start], val_fre_lst[pivot] = val_fre_lst[pivot], val_fre_lst[start]
    l, r = start, end
    while l < r:
        while l < r and val_fre_lst[l][1] >= val_fre_lst[start][1]:
            l += 1
        while l < r and val_fre_lst[r][1] <= val_fre_lst[start][1]:
            r -= 1
        val_fre_lst[l], val_fre_lst[r] = val_fre_lst[r], val_fre_lst[l]
    val_fre_lst[l], val_fre_lst[start] = val_fre_lst[start], val_fre_lst[l]
    if l == k:
        return val_fre_lst
    elif l < k:
        fastrank(val_fre_lst, k, l + 1, end)
    else:
        fastrank(val_fre_lst, k, start, l - 1)
# print(fastrank(val_fre_lst, 2, 0, m - 1))