'''
#############################################################################################################
**题目03：（数组）
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
**示例：
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3
**条件：
0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
#############################################################################################################
'''

'''
双指针方法：
利用字典来存储频次信息，移动快指针，当发现有重复字符时，开始移动慢指针，直到无重复字符为止
记录此时的字符串长度
复杂度分析：
时间复杂度：O(N)
空间复杂度：O(N)
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        m = len(s)
        slow, fast, fre_dic = 0, 0, {}
        res = 0
        while fast < m:
            fast_value = s[fast]
            fast += 1
            fre_dic[fast_value] = fre_dic.get(fast_value, 0) + 1
            while fre_dic[fast_value] > 1:
                slow_value = s[slow]
                slow += 1
                fre_dic[slow_value] -= 1
            res = max(res, fast - slow)
        return res
print(Solution().lengthOfLongestSubstring('abcbcd'))












