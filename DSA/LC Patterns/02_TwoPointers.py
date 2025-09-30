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


def new_three_sum(nums):
    nums.sort()
    ans = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]: continue
        j = i+1
        k = len(nums)-1
        target = -nums[i]
        while j < k:
            if nums[j] + nums[k] > target:
                k -= 1
            elif nums[j] + nums[k] < target:    
                j += 1
            else:
                ans.append([nums[i],nums[j],nums[k]])
                
                j += 1
                k -= 1
                while nums[j-1] == nums[j] and j < k:
                    j += 1
                while nums[k+1] == nums[k] and j < k:
                    k -= 1
                
    return ans
print(new_three_sum([-1,0,1,2,-1,-4,2]))


def four_sum(nums,target):
    nums.sort()
    ans = []
    for i in range(len(nums)):
        if i > 0 and nums[i-1] == nums[i]: continue
        for j in range(i+1,len(nums)):
            if j != i+1 and nums[j-1] == nums[j]: continue
            k = j + 1
            l = len(nums) - 1
           
            while k < l:
                mysum = nums[i] + nums[j] + nums[k] + nums[l]
                if mysum > target:
                    l -= 1
                elif mysum < target:
                    k += 1
                else:
                    ans.append([nums[i],nums[j],nums[k],nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k-1] == nums[k]:
                        k += 1
                    while k < l and nums[l+1] == nums[l]:
                        l -= 1
    return ans
print(four_sum([1,1,1,2,2,2,3,3,3,4,5,5,4,4],8))



# Sort array having 0,1,2
# Dutch national flag algo
def dutch_algo(nums):
    low,mid = 0,0
    high = len(nums)-1
    while mid <= high:
        if nums[mid] == 0:
            nums[mid],nums[low] = nums[low],nums[mid]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high -= 1
    return nums
# print(dutch_algo([1,2,0,1,2,2,2,1,0,0,1,0,2]))









