def binary_search_iterative(nums, k):  # O(logN) O(1)
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if k > nums[mid]:
            left = mid + 1
        elif k < nums[mid]:
            right = mid - 1
        else:
            return mid
    return -1
# print(binary_search_iterative([1,2,3,3,3,4,5,5,5,6,9,10],5))


def binary_search_recursive(left, right, k, nums):  # O(logN) O(logN)
    if right >= left:
        mid = (left + right) // 2
        if nums[mid] == k:
            return mid
        elif nums[mid] > k:
            return binary_search_recursive(left, mid - 1, k, nums)
        else:
            return binary_search_recursive(mid + 1, right, k, nums)
    else:
        return -1
# print(binary_search_recursive(0,10,5,[1,2,3,3,3,4,5,5,5,6,9,10]))


def binary_search_first(nums,target,findfirst):
    start,end = 0,len(nums)-1
    ans = -1
    while start <= end:
        mid = (start+end) // 2
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            ans = mid
            if findfirst:
                end = mid - 1
            else:
                start = mid + 1
    return ans
# print(binary_search_first([1,2,3,3,3,4,5,5,5,6,9,10],5,False))

def binary_search_lower_bound(nums,k):
    # find the smallest index lesser or equal to k arr[ind] >= k
    l,h = 0, len(nums)-1
    ans = len(nums)

    while l <= h:
        mid = (l+h) // 2
        if nums[mid] >= k:
            ans = mid
            h = mid - 1
        else:
            l = mid + 1
    return ans
# print(binary_search_lower_bound([1,2,3,5,6,9,12,45],3))

def binary_search_upper_bound(nums,k):
    # find the smallest index greater than k arr[ind] > k
    l,h = 0, len(nums)-1
    ans = len(nums)

    while l <= h:
        mid = (l+h)//2
        if nums[mid] > k:
            ans = mid
            h = mid - 1
        else:
            l = mid + 1
    return ans
# print(binary_search_upper_bound([1,2,3,5,6,9,12,45],3))

# find first and last occurrence of the element in array
def first_last_occ(nums,k):
    # first occ => lower bound, last occ => upper bound
    def lower_bound(nums,k):
        l,h = 0,len(nums)-1
        ans = len(nums)

        while l <= h:
            mid = (l+h)//2
            if nums[mid] >= k:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans
    def upper_bound(nums,k):
        l,h = 0, len(nums)-1
        ans = len(nums)

        while l<=h:
            mid = (l+h)//2
            if nums[mid] > k:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans

    lb = lower_bound(nums,k)
    ub = upper_bound(nums,k)
    if lb == len(nums) or nums[lb] != k:
        return [-1,-1]
    else:
        return [lb,ub-1]
# print(first_last_occ([1,2,3,4,4,4,4,5,6,6,6,7],6))


def first_occ(nums,k):
    l,h = 0,len(nums)-1
    first = -1
    while l<=h:
        mid = (l+h)//2
        if nums[mid] == k:
            first = mid
            h = mid - 1
        elif nums[mid] > k:
            h = mid - 1
        else:
            l = mid + 1
    return first
# print(first_occ([2,8,8,8,8,8,11,13],8))

def last_occ(nums,k):
    l,h = 0,len(nums)-1
    last = -1
    while l<=h:
        mid = (l+h)//2
        if nums[mid] == k:
            last = mid
            l = mid + 1
        elif nums[mid] < k:
            l = mid + 1
        else:
            h = mid - 1
    return last
# print(last_occ([2,8,8,8,8,8,11,13],8))

# search in rotated array with unique elements
def search_rotated_array_unique(nums,k):
    # identify sorted half then if it lies in sorted half take that half else other half is sorted
    l,h = 0, len(nums)-1

    while l<=h:
        mid = (l+h)//2
        if nums[mid] == k:
            return mid
        if nums[l] <= nums[mid]: # left half is sorted
            if nums[l] <= k <= nums[mid]:
                h = mid - 1
            else:
                l = mid + 1
        else:                   # right half is sorted
            if nums[mid] <= k <= nums[h]:
                l = mid + 1
            else:
                h = mid - 1
    return -1
# print(search_rotated_array_unique([7,8,9,1,2,3,4,5,6],95))

# # search in rotated array with unique elements
def search_rotated_array_dup(nums,k):
    l,h = 0, len(nums)-1

    while l <= h:
        mid = (l+h)//2
        if nums[mid] == k:
            return True
        if nums[l] == nums[mid] == nums[h]: # one edge case different from unique, shrink down search space
            l += 1                          # from both sides in case 3 points are same, we cant get which
            h -= 1                          # half is sorted
            continue
        if nums[l] <= nums[mid]:
            if nums[l] <= k <= nums[mid]:
                h = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] <= k <= nums[h]:
                l = mid + 1
            else:
                h = mid - 1
    return False
# print(search_rotated_array_unique()[3,3,3,3,3,3,3,3,3,3],3)

# find minimum in rotated sorted array
def min_rotate(nums):
    l,h = 0, len(nums)-1
    ans = float("inf")
    while l <= h:
        mid  = (l+h)//2
        if nums[l] <= nums[h]:  # optimization when both parts are sorted
            return nums[l]
        if nums[l] == nums[mid] == nums[h]: # for duplicates
            l += 1
            h -= 1
            continue
        if nums[l] <= nums[mid]:
            ans = min(ans,nums[l])
            l = mid + 1
        else:
            ans = min(ans,nums[mid])
            h = mid - 1
    return ans
# print(min_rotate([1,1,1,1,1,1,1,1,1,2,3]))


# find single element in an array
def single_element(nums):
    if len(nums) == 1: return nums[0]
    if nums[0] != nums[1]: return nums[0]
    if nums[-1] != nums[-2]: return nums[-1]

    l,h = 1,len(nums)-2
    while l<=h:
        mid = (l+h)//2
        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        if (mid % 2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 == 1 and nums[mid] == nums[mid-1]):
            l = mid + 1
        else:
            h = mid - 1
    return -1
# print(single_element([1,2,2,3,3,4,4,5,5,6,6]))

# find peak element
def peak_element(nums):
    if len(nums) == 1: return nums[0]
    if nums[0] > nums[1]: return nums[0]
    if nums[-1] > nums[-2]: return nums[-1]
    l,h = 1,len(nums)-2
    while l <= h:
        mid = (l+h)//2
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid] > nums[mid-1]:
            l = mid+1
        else:
            h = mid-1
    return -1
print(peak_element([1,2,33,4,5,6,8,7,5,1]))




