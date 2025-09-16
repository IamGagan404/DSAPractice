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
# print(min_win(s = "ADOBECODEBANC", t = "ABC"))



# longest substrign without repeating charater
def long_subs(s):
    seen = [-1] * 256
    l,r = 0,0
    maxl = 0
    m,n = 0,0
    while r < len(s):
        if seen[ord(s[r])] != -1:
            if seen[ord(s[r])] >= l:
                l = seen[ord(s[r])] + 1
        cur_len = r-l+1
        maxl = max(maxl,cur_len)
        seen[ord(s[r])] = r
        r += 1
    return maxl,s[l:r+1]
# print(long_subs("cadbzabcd"))


# max con ones 3
def max_con_3(nums,k): # O(2N)
    l,r = 0,0
    z = 0
    maxl = 0

    while r < len(nums):
        if nums[r] == 0:
            if z == k:
                while nums[l] == 1:
                    l += 1
                l += 1
            else:
                z += 1
        maxl = max(maxl,r-l+1)
        r += 1
    return maxl
# print(max_con_3(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3) )

def max_cons_3_optimal(nums,k): # O(N)
    l,r,z,maxl = 0,0,0,0
    while r < len(nums):
        if nums[r] == 0:
            z += 1
        if z > k:
            if nums[l] == 0:
                z -= 1
            l += 1
        if z <= k:
            maxl = max(maxl,r-l+1)
        r += 1
    return maxl
# print(max_cons_3_optimal(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3) )


# fruits into basket
def fruits_basket(fruits,k):
    fruits = list(fruits)
    l,r = 0,0
    maxl = 0
    fmap = {}
    while r < len(fruits):
        fmap[fruits[r]] = 1 + fmap.get(fruits[r],0)
        if len(fmap.keys()) > k:
            fmap[fruits[l]] -= 1
            if fmap[fruits[l]] == 0:
                del fmap[fruits[l]]
            l += 1
        if len(fmap.keys()) <= k:
            maxl = max(maxl,r-l+1)
        r += 1
    return maxl
# print(fruits_basket(fruits= "abcddefg" , k = 3))

# This is from office laptop

