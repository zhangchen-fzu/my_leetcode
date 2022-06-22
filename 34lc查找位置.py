'''
#############################################################################################################
**题目34：（数组）
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
**示例：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
**条件：
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
**进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
#############################################################################################################
'''
'''
暴力循环方法：
在循环过程中去判断值是否为target,
若值为target,在去判断他是在开头位置还是在结尾位置
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(1)
'''
class Solution1(object):
    def searchRange(self, nums, target):
        res=[-1,-1]
        for i in range(len(nums)):
            if nums[i]==target:
                if res[0]!=-1: ##结尾
                    res[1]=i
                else: ##开头和结尾都赋值，放置某元素只出现一次
                    res[0]=i
                    res[1]=i
        return res

'''
二分法寻找左右边界值：
寻找左边界，是将右指针不断左压，在nums[i]==target时；
寻找右指针，是将左指针不断右压，在nums[i]==target时；
复杂度分析：
时间复杂度：O(logN)
空间复杂度：O(1)
'''
class Solution2(object):
    def searchRange(self, nums, target):
        l = self.get_pos(nums, target, 0)
        r = self.get_pos(nums, target, 1)
        return [l, r]

    def get_pos(self, nums, target, sign):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                if sign == 1:  ##右边界
                    if mid == len(nums) - 1 or nums[mid + 1] > target:
                        return mid
                    l = mid + 1
                else:  ##左边界
                    if mid == 0 or nums[mid - 1] < target:
                        return mid
                    r = mid - 1
        return -1