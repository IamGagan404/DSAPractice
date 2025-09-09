# A fixed sized window iterates over the array. The computation of next window depends on the previous window.
# Usually asked for max/min of the window with  size k.

# 643. Maximum Average Subarray I
def findMaxAverage(nums,k):
    sum_window = cur_win = sum(nums[:k])

    for i in range(k,len(nums)):
        cur_win += nums[i] - nums[i-k]
        sum_window = max(sum_window,cur_win)
    return sum_window/k

# 3. Longest Substring without Repeating Characters


