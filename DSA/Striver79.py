"""
https://takeuforward.org/interview-sheets/strivers-79-last-moment-dsa-sheet-ace-interviews
"""
# Arrays and Hashing

# 31 next permutation in place - two pointers, IN PLACE
# find the breakpoint: start from end, find a point where value is smaller than previous FROM END
# that is the prefix
# find next immediate number greater than breakpoint
# swap those elements, reverse the rest of the array
def next_per(nums):
    """# find breakpoint
    breakpoint = -1
    for i in range(len(nums)-1,-1,-1):
        print(nums[i],nums[i-1])
        if nums[i] > nums[i-1]:
            breakpoint = nums[i]
            break
    breakpoint = nums[i-1]
    prefix = nums[:i-1]
    print(prefix)
    suffix = nums[i-1:]
    print(suffix)
    # find immediate greater than suffix[0]

    for i in range(len(suffix)-1,-1,-1):
        if suffix[i] > suffix[0]:
            new_first = suffix[i]
            break
    suffix.remove(new_first)
    suffix = sorted(suffix)
    print([new_first]+suffix)
    print(prefix+suffix)
"""
    # find breakpoint
    breakpoint = -1
    n = len(nums)
    for i in range(n-2,-1,-1):
        if nums[i] < nums[i+1]:
            breakpoint = i
            break
    if breakpoint == -1:
        nums = nums.reverse()
        return nums
    # find greater that breakpoint and swap
    for i in range(n-1,breakpoint,-1):
        if nums[i] > nums[breakpoint]:
            nums[i],nums[breakpoint] = nums[breakpoint],nums[i]
            break
    # reverse rest of the array
    nums[breakpoint+1:] = reversed(nums[breakpoint+1:])
    return nums

# 15 3sum
def three_sum_divide(nums):
    re = set()
    n = []
    p = []
    z = []
    for num in nums:
        if num < 0: n.append(num)
        elif num > 0 : p.append(num)
        else: z.append(num)
    N, P = set(n), set(p)
    if z:
        for num in P:
            if -num in N:
                re.add((-num,0,num))
    if len(z) >= 3:
        re.add((0,0,0))
    for i in range(len(p)-1):
        for j in range(i+1,len(p)):
            target = -(p[i]+p[j])
            if target in N:
                re.add(tuple(sorted([p[i],p[j],target])))
    for i in range(len(n)-1):
        for j in range(i+1,len(n)):
            target = -(n[i]+n[j])
            if target in P:
                re.add(tuple(sorted([n[i],n[j],target])))
    return re

# 53 kdane algorithm: subarray with the highest sum
def kdane(nums):
    n = len(nums)
    maxi = -float('inf')
    sum = 0
    start,end = -1,-1
    for i in range(n):
        if sum ==0 : start = i
        sum += nums[i]

        if sum > maxi:
            end = i
            maxi = sum
        if sum<0:
            sum=0
    return maxi,start,end

#





