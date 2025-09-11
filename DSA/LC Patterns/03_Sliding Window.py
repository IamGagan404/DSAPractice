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




# 76. Minimum Window Substring
def min_win(s,t):
    if len(t) > len(s):
        return ""
    elif len(t) == len(s):
        return s if sorted(s) == sorted(t) else ""
    else:
        window,t_dict = {},{}
        for c in t:
            t_dict[c] = 1 + t_dict.get(c,0)
        have,need = 0, len(t_dict)
        res,resLen = [-1,-1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in t_dict and t_dict[c] == window[c]:
                have += 1

            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                window[s[l]] -= 1
                if s[l] in t_dict and t_dict[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""
print(min_win(s = "ADOBECODEBANC", t = "ABC"))



