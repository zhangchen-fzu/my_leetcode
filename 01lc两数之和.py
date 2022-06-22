'''
#############################################################################################################
**题目：（数组）
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
**示例：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
**条件：
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
#############################################################################################################
'''


'''
暴力解法：
第一个for循环去控制第一个数
第二个for循环去后面搜寻是否有第二个数，使得【一+二=target】
复杂度分析：
时间复杂度：两个for循环嵌套O(N^2)
空间复杂度：O(1)
'''
class Solution1(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []


'''
排序+双指针方法：
对于有序数组寻找target的情况，可以使用双指针的方法，但本题是无序数组，排序后数值的原有index会发生变化，因此需记录原有的数组信息。
可copy原有数组给新变量，找到新变量的index之后，需要去原数组中寻找原index,由于a.index()方法只会搜索到第一个为值为某值的index，
因此在搜索完后需要给搜索到的值赋值一个该数组不会出现的值，可避免[3,3]target=6返回[0,0]的情况。
复杂度分析：
时间复杂度：sort()底层是归并排序，时间复杂度为O(NlogN)
空间复杂度：O(N)'''
class Solution2(object):
    def twoSum(self, nums, target):
        nums1=nums[:]
        nums1.sort()
        l,r=0,len(nums1)-1
        while l<r:
            if nums1[l]+nums1[r]<target:
                l+=1
            elif nums1[l]+nums1[r]>target:
                r-=1
            else:
                break
        result1=nums.index(nums1[l])
        nums[result1]=float('inf')
        result2=nums.index(nums1[r])
        return [result1,result2]


'''
dic存储索引信息方法：
暴力搜索时，对于第一个数搜索了后面的所有数，对于第二个数搜索了后面的所有数，存在重复搜索的情况，这种情况可用dic实现O(1)快速搜索。
用dic存储每个数的索引，拿出一个数，去dic中搜索【target-该数】是否存在。由于正确结果只有一个，因此可以边遍历边搜索，
字典重复值覆盖即可，因为该值不可能是最终的结果。
复杂度分析：
时间复杂度：一个for循环O(N)
空间复杂度：开辟dic存放数值及index信息O(N)
'''
class Solution3(object):
    def twoSum(self, nums, target):
        dic={}
        for i in range(len(nums)):
            if target-nums[i] in dic:
                return [i,dic[target-nums[i]]]
            dic[nums[i]]=i
        return []