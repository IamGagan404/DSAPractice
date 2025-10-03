# assign cookies
def cookies(g,s):
    g.sort()
    s.sort()
    re = 0
    l,r = 0,0
    while l < len(s):
        if s[l] >= g[r]:
            re += 1
            r += 1
        l+= 1 

# jump game 1
def jg1(nums):
    max_ind = nums[0]
    for i in range(len(nums)):
        if max_ind < i:
            return False
        max_ind = max(max_ind,nums[i]+i)
    return True

