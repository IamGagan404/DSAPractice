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
    pass

def ninja_training(nums): # striver
    def recursion(nums):
        def helper(day,last):
            if day == 0:
                maxi = 0
                for i in range(0,3):
                    if i != last:
                        maxi = max(maxi,nums[0][i])
                return maxi
            maxi = 0
            for i in range(0,3):
                if i != last:
                    points = nums[day][i] + helper(day-1,i)
                    maxi = max(maxi,points)
            return maxi
        return helper(len(nums)-1,3)
    

    def memoization(nums):
        n = len(nums)
        dp = [[-1]*4 for i in range(n)]
        def helper(day,last,dp):
            if dp[day][last] != -1: return dp[day][last]
            if day == 0:
                maxi = 0
                for i in range(0,3):
                    if i != last:
                        maxi = max(maxi,nums[0][i])
                dp[day][last] = maxi
                return dp[day][last]
            
            maxi = 0
            for i in range(0,3):
                if i != last:
                    points = nums[day][i] + helper(day-1,i,dp)
                    maxi = max(maxi,points)
            dp[day][last] = maxi
            return maxi

        return helper(len(nums)-1,3,dp)

    def tabulation(nums):
        n = len(nums)
        dp = [[-1]*4 for _ in range(n)]

        dp[0][0] = max(nums[0][1],nums[0][2])
        dp[0][1] = max(nums[0][0],nums[0][2])
        dp[0][2] = max(nums[0][1],nums[0][0])
        dp[0][3] = max(nums[0][0],nums[0][1],nums[0][2])

        for day in range(1,n):
            for last in range(0,4):
                dp[day][last] = 0
                for i in range(0,3):
                    if i != last:
                        points = nums[day][i] + dp[day-1][i]
                        dp[day][last] = max(dp[day][last],points)
        return dp[n-1][3]
    
    def space_optimization(nums):
        n = len(nums)
        dp = [-1]*4

        dp[0] = max(nums[0][1],nums[0][2])
        dp[1] = max(nums[0][0],nums[0][2])
        dp[2] = max(nums[0][1],nums[0][0])
        dp[3] = max(nums[0][0],nums[0][1],nums[0][2])

        for day in range(1,n):
            temp = [0]*4
            for last in range(0,4):
                temp[last] = 0
                for i in range(0,3):
                    if i != last:
                        points = nums[day][i] + dp[i]
                        temp[last] = max(temp[last],points)
            dp = temp
        return dp[3]




    return space_optimization(nums)

def grid(m,n):  # Unique paths LC
    dp = [[-1]*n for _ in range(m)]

    # re = 0
    # def helper(a,b):
    #     if a == 0 and b == 0:
    #         return 1
    #     if a < 0 or b < 0:
    #         return 0
    #     if dp[a][b] != -1 : return dp[a][b]
    #     up = helper(a-1,b)
    #     left = helper(a,b-1)
    #     dp[a][b] = up+left
    #     return  dp[a][b]
    # return helper(m-1,n-1)

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[0][0] = 1
                continue
            up = 0
            left = 0
            if i > 0: up = dp[i-1][j]
            if j > 0: left = dp[i][j-1]
            dp[i][j] = up+left
    return dp[m-1][n-1]

def minimum_path_sum(nums):
    m = len(nums)
    n = len(nums[0])
    dp = [[-1]*n for _ in range(m)]
    # def helper(i,j):
    #     if i == 0 and j == 0:
    #         return nums[i][j]
    #     if i < 0 or j < 0:
    #         return float('inf')
    #     if dp[i][j] != -1: return dp[i][j]
    #     up = nums[i][j] + helper(i-1,j)
    #     left = nums[i][j] + helper(i,j-1)
    #     dp[i][j] = min(left,up)
    #     return min(left,up)
    # return helper(len(nums)-1,len(nums[0])-1)

    for i in range(m):
        for j in range(n):
            print(dp)
            if i == 0 and j == 0:
                dp[i][j] = nums[i][j]
            else:
                up,left = nums[i][j],nums[i][j]
                if i > 0:
                    up = nums[i][j] + dp[i-1][j]
                else:
                    up += int(1e9)
                if j > 0:
                    left = nums[i][j] + dp[i][j-1]
                else:
                    left += int(1e9)
                dp[i][j] = min(up,left)
    return dp[m-1][n-1]

def minimumTotal(tri):
        n = len(tri[-1])
        dp = [[-1]*n for _ in range(n)]

        # def helper(i,j):
        #     if i == n-1: return tri[i][j]
        #     if dp[i][j] != -1: return dp[i][j]
        #     down = tri[i][j] + helper(i+1,j)
        #     dg = tri[i][j] + helper(i+1,j+1)
        #     dp[i][j] = min(down,dg)
        #     return min(down,dg)
        # return helper(0,0)
        for j in range(n):
            dp[n-1][j] = tri[n-1][j]
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                down = tri[i][j] + dp[i+1][j]
                dg = tri[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down,dg)
        return dp[0][0]


def minFallingPathSum(matrix): # LC 931
        n = len(matrix)
        dp = [[-1] * n for _ in range(n)]
        # def helper(i,j):
        #     if i == n-1: return matrix[i][j]
        #     if dp[i][j] != -1: return dp[i][j]
        #     down = matrix[i][j] + helper(i+1,j)
        #     dgl,dgr = float('inf'),float('inf')
        #     if j > 0: dgl = matrix[i][j] + helper(i+1,j-1)
        #     if j < n-1: dgr = matrix[i][j] + helper(i+1,j+1)
        #     dp[i][j] = min(down,dgl,dgr)
        #     return min(down,dgl,dgr)
        # re = float('inf')
        # for i in range(n):
        #     re = min(re,helper(0,i))
        # return re

        for i in range(n):
            dp[-1][i] = matrix[-1][i]
        for i in range(n-2,-1,-1):
            for j in range(n-1,-1,-1):
                down = matrix[i][j] + dp[i+1][j]
                dgl,dgr = float('inf'),float('inf')
                if j > 0: dgl = matrix[i][j] + dp[i+1][j-1]
                if j < n-1: dgr = matrix[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down,dgl,dgr)
        return min(dp[0])

# DP on sequences
def subset_sum_k(arr,target):
    dp = [[0]*(target+1) for _ in range(len(arr))]
    # print(dp)
    # def helper(ind,target):
    #     print(dp)
    #     if target == 0: return True
    #     if ind == 0: return target == arr[0]
    #     if dp[ind][target] != 1: return dp[ind][target]
    #     not_take = helper(ind-1,target)
    #     take = False
    #     if arr[ind] <= target:
    #         take = helper(ind-1,target-arr[ind])
    #     dp[ind][target] = not_take or take
    #     return not_take or take
    
    # return helper(len(arr)-1,target)

    for i in range(len(arr)) : dp[i][0] = True
    dp[0][arr[0]] = True

    for ind in range(1,len(arr)):
        for t in range(1,target+1):
            not_take = dp[ind-1][t]
            take = False
            if t >= arr[ind]:
                take = dp[ind-1][t-arr[ind]]
            dp[ind][t] = not_take or take
    print(dp)
    return bool(dp[len(arr)-1][target])

def knapsack(W, val, wt):
    # code here
    dp = [[0] * (W+1) for _ in range(len(wt))]
    # def helper(ind,bg):
    #     if ind == 0: 
    #         if wt[0] <= bg: return val[0]
    #         else: return 0
    #     if dp[ind][bg] != -1: return dp[ind][bg]
    #     not_take = helper(ind-1,bg)
    #     take = -1e9
    #     if wt[ind] <= bg: take = val[ind] + helper(ind-1,bg-wt[ind])
    #     dp[ind][bg] = max(take,not_take)
    #     return dp[ind][bg]
    # return helper(len(wt)-1,W)
    
    
    # for i in range(wt[0],W+1): dp[0][i] = val[0]
    # for ind in range(1,len(wt)):
    #     for bg in range(0,W+1):
    #         not_take = dp[ind-1][bg]
    #         take = -1e9
    #         if wt[ind] <= bg: take = val[ind] + dp[ind-1][bg-wt[ind]]
    #         dp[ind][bg] = max(take,not_take)
    # return dp[len(wt)-1][W]
    
    prev = [0] * (W+1)
    for i in range(wt[0],W+1): prev[i] = val[0]
    for ind in range(1,len(wt)):
        cur = [0] * (W+1)
        for bg in range(0,W+1):
            not_take = prev[bg]
            take = -1e9
            if wt[ind] <= bg: take = val[ind] + prev[bg-wt[ind]]
            cur[bg] = max(take,not_take)
        prev = cur
    return prev[W]


###########
# DP on strings

# Longest common sudsequence
def lcs(text1,text2):
    n = len(text1)
    m = len(text2)
    dp = [[-1] * (m+1) for _ in range(n+1) ]
    # def helper(i,j):
    #     if i == 0 or j == 0: return 0
    #     if dp[i][j] != -1: return dp[i][j]
    #     if text1[i-1] == text2[j-1]:
    #         dp[i][j] = 1 +  helper(i-1,j-1)
    #         return dp[i][j]
    #     dp[i][j] = max(helper(i-1,j),helper(i,j-1))
    #     return dp[i][j]
    # return helper(len(text1),len(text2))
    for i in range(m+1): dp[0][i] = 0
    for j in range(n+1): dp[j][0] = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[n][m]

# for printing lsc dp last row is used, go diagonal if matching else max in up or left refer notes
# i = n
# j = m
# ans = ""
# while i > 0 and j > 0:
#     if str1[i-1] == str2[j-1]:
#         ans.append(str1[i-1])
#         i -= 1
#         j -= 1
#     elif dp[i-1][j] > dp[i][j-1]:
#         i -= 1
#     else:
#         j -= 1
# return ans[::-1]


# longest common substring
def lc_substring(text1,text2): # intuition from dp table
    n = len(text1)
    m = len(text2)
    dp = [[-1] * (m+1) for _ in range(n+1) ]
    for i in range(m+1): dp[0][i] = 0
    for j in range(n+1): dp[j][0] = 0
    ans = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                ans = max(ans,dp[i][j])
            else:
                dp[i][j] = 0
    return ans

# shortest supersubsequesnce: 
# modification in print lcs tabulation
# when going up or left: add that char also in ans string
# in end add chars remaining in the words in ans string


# string matching pattern
# 115 distinct subsequences
def dis_subs(s,t):
    def helper(i,j):
        if j < 0: return 1
        if i < 0: return 0
        
        if s[i] == t[j]:
            return  (helper(i-1,j-1) + helper(i-1,j))   
        else:
            return helper(i-1,j)
    return helper(len(s)-1,len(t)-1)


if __name__ == '__main__':
    # print(climbing_stairs_bu(5))
    # print(climbing_stairs_td(5))
    # print(frog_bu([30, 10, 60, 10, 60, 50]))
    # print(frog_td([30, 10, 60, 10, 60, 50]))
    # print(k_frog_bu( [30, 10, 60, 10, 60, 50],2))
    # print(part_sum(nums=[1, 5, 11, 5]))
    # print(ninja_training(nums=[[10, 40, 70],[20, 50, 80],[30, 60, 90]]))
    # print(minimum_path_sum(nums=[[5, 9, 6], [11, 5, 2]]))
    # print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    # print(minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
    # print(subset_sum_k([1,2,2,3],3))
    # print(knapsack(W = 4, val = [1, 2, 3], wt = [4, 5, 1] ))
    # print(lcs("sea","eat"))
    # print(lc_substring("abcjklp","acjkp"))
    print(dis_subs(s = "rabbbit", t = "rabbit"))
    pass

