def canPartition(nums):
    m = len(nums)
    sum_val = sum(nums)
    if sum_val % 2 != 0:
        return False

    mid_val = sum_val // 2
    dp = [[False] * (mid_val + 1) for _ in range(m + 1)]

    for i in range(mid_val + 1):
        dp[i][0] = True

    for i in range(1, m + 1):
        for j in range(1, mid_val + 1):
            if j - nums[i - 1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i - 1]]
    return dp[m][mid_val]


def canPartition1(nums):
    m = len(nums)
    sum_val = sum(nums)
    if sum_val % 2 != 0:
        return False

    mid_val = sum_val // 2
    dp = [([True] + [False] * mid_val) for _ in range(2)]

    for i in range(1, m + 1):
        for j in range(1, mid_val + 1):
            if j - nums[i - 1] < 0:
                dp[1][j] = dp[0][j]
            else:
                dp[1][j] = dp[0][j] | dp[0][j - nums[i - 1]]
        dp[0][:] = dp[1][:]
    return dp[0][-1]




def canPartition2(nums):
    m = len(nums)
    sum_val = sum(nums)
    if sum_val % 2 != 0:
        return False

    mid_val = sum_val // 2
    dp = [True] + [False] * mid_val

    for i in range(1, m + 1):
        for j in range(mid_val, -1, -1):
            if j - nums[i - 1] >= 0:
                dp[j] = dp[j] | dp[j - nums[i - 1]]
    return dp[-1]