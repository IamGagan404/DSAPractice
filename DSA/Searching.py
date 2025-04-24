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




