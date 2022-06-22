def rob(self, nums):
    m = len(nums)
    if m == 1:
        return nums[0]
    max_res = max(0, sub(nums, 1, m - 1), sub(nums, 0, m - 2))
    return max_res

def sub(nums, start, end):
    dp = [0] * (end - start + 1 + 2)
    for i in range(end - start, -1, -1):
        dp[i] = max(dp[i + 1], dp[i + 2] + nums[start + i])
    return dp[0]