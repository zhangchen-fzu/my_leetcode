'''
#############################################################################################################
**题目912：（数组）
给你一个整数数组 nums，请你将该数组升序排列
**示例：
输入：nums = [5,2,3,1]
输出：[1,2,3,5]
**条件：
1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
#############################################################################################################
'''

'''
归并排序：
1.建立一个临时数组tmp用于存储排序后的数组分片
2.进入循环，分别从两个数组分片的头部开始遍历，比较大小，不断将小的值加到tmp中
3.两个数组分片未必完全等分，所以在循环完成后将剩余的值也加到tmp中
复杂度分析：
时间复杂度：O(NlogN)
空间复杂度：O(N)
'''
class Solution2(object):
    def sortArray(self, nums):
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums, low, high):
        if low < high:
            mid = (low + high) // 2
            self.mergeSort(nums, low, mid)
            self.mergeSort(nums, mid + 1, high)
            self.mergeTwoArrays(nums, low, mid, high)

    def mergeTwoArrays(self, nums, low, mid, high):
        i, j, tmp = low, mid + 1, []
        while i <= mid and j <= high:
            if nums[i] <= nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        tmp += nums[i:mid+1] + nums[j:high+1]
        nums[low:high+1] = tmp