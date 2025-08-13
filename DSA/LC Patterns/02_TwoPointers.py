# 167. Two Sum II - Input Array is Sorted
def two_sum_2(nums,target):
    l,r = 0,len(nums)-1
    while l < r:
        if nums[l]+nums[r] == target:
            return [l+1,r+1]
        elif nums[l]+nums[r] > target:
            r = r-1
        else:
            l += 1
    return [l+1,r+1]
# print(two_sum_2(nums = [0,0,3,4], target = 0))


# 15. 3 Sum
def three_sum(nums):
    nums.sort()
    re = []

    for i in range(len(nums)-2):
        l,r = i+1,len(nums)-1
        while l < r:
            if nums[l]+nums[r] == -nums[i]:
                re.append([nums[i],nums[l],nums[r]])
            elif nums[l]+nums[r] > -nums[i]:
                r = r-1
            else:
                l += 1
    return re
print(three_sum(nums = [-1,0,1,2,-1,-4]))

# 11. Container with most water









