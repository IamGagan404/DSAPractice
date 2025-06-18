"""
Usually DP problems asks for number of ways or multiple ways to solve a problem.
Try to think of a recursive solution, once done, convert in DP solution.
3 steps to solve the problem
    1. try to get into terms of indexes
    2. try for all possible choices at every index
    3. if problem asks for count, return sum or asks for max/min return from that index array.

# Tabulation   bottom up   often involves iterative approach
# Memoization  top down    often involves recursion

"""


# 70 Climbing stairs
# Bottom-up
def climbing_stairs_bu(n):
    dp = [-1] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# Top-Down
def climbing_stairs_td(n):
    dp = [-1] * (n + 1)

    def rec(dp, m):
        if m <= 1:
            return m
        if dp[m] != -1:
            return dp[m]
        dp[m] = rec(dp, m - 1) + rec(dp, m - 2)
        return dp[m]

    return rec(dp, n)


# Frog jumps 1 or 2 steps, energy is consumed as difference between steps value. Min energy to reach step N.
def frog_bu(steps):
    n = len(steps)
    dp = [-1 for _ in range(n)]
    dp[0] = 0
    dp[1] = steps[0]
    for i in range(1, n):
        j1 = dp[i - 1] + abs(steps[i] - steps[i - 1])
        j2 = dp[i - 2] + abs(steps[i] - steps[i - 2])
        dp[i] = min(j1, j2)
    return dp[n - 1]


def frog_td(steps):
    dp = [-1 for i in range(len(steps))]

    def helper(steps, n, dp):
        if n == 0:
            return 0
        if dp[n] != -1:
            return dp[n]
        else:
            j2 = float('inf')
            j1 = abs(steps[n] - steps[n - 1]) + helper(steps, n - 1, dp)
            if n > 1:
                j2 = abs(steps[n] - steps[n - 2]) + helper(steps, n - 2, dp)
            dp[n] = min(j1, j2)
            return dp[n]

    return helper(steps, len(steps) - 1, dp)


# frog can jump k steps
def k_frog_bu(steps, k):  # not working
    n = len(steps)
    dp = steps[:k] + [-1 for i in range(n - k)]
    for i in range(k, n):
        jmin = float('inf')
        for j in range(1, k + 1):
            jcur = abs((steps[i] - steps[i - j])) + dp[i - j]
            jmin = min(jcur, jmin)
        dp[i] = jmin
    return dp[n - 1]


# 416 partition equal subset sum
def part_sum(nums):  # 0/1 knapsack problem
    total_sum = sum(nums)
    if total_sum % 2 == 1:
        return False
    else:
        target_sum = total_sum // 2
        dp = [False] * (target_sum + 1)
        dp[0] = True
        for num in nums:
            for curSum in range(target_sum, num - 1, -1):
                dp[curSum] = dp[curSum] or dp[curSum - num]
        return dp[target_sum]

# 3418. Maximum Amount of Money Robot Can Earn
def robot_money(coins):



if __name__ == '__main__':
    # print(climbing_stairs_bu(5))
    # print(climbing_stairs_td(5))
    # print(frog_bu([30, 10, 60, 10, 60, 50]))
    # print(frog_td([30, 10, 60, 10, 60, 50]))
    # print(k_frog_bu( [30, 10, 60, 10, 60, 50],2))
    # print(part_sum(nums=[1, 5, 11, 5]))
    pass
