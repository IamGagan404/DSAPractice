def binary_search_iterative(nums, k):  # O(logN) O(1)
    left = 0
    right = len(nums) - 1
    mid = 0

    while left <= right:
        mid = (left + right) // 2
        if k > nums[mid]:
            left = mid + 1
        elif k < nums[mid]:
            right = mid - 1
        else:
            return mid
    return -1


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


def binary_search(nums,target,findfirst):
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

print(binary_search([1,2,3,3,3,4,5,5,5,6,9,10],5,False))
