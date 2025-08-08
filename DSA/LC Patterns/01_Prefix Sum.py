# 303. Range Sum Query - Immutable
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = self.get_prefix(nums)
        print(self.prefix)

    def get_prefix(self, nums):
        re = 0
        prefix = [None] * len(nums)
        for i in range(len(nums)):
            re += nums[i]
            prefix[i] = re

        return prefix

    # -2 -2 1 -4 -2 -3
    # 0 -2 -2  1 -4 -2

    def sumRange(self, left: int, right: int) -> int:
        if left == 0: return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]


# 525. Contiguous Array
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pref_sum = {}
        max_len = 0
        pref = 0

        for i, num in enumerate(nums):
            pref += 1 if num == 1 else -1
            if pref == 0:
                max_len = i + 1
            elif pref in pref_sum:
                max_len = max(max_len, i - pref_sum[pref])
            else:
                pref_sum[pref] = i
        return max_len

# 560. Subarray Sum Equals K
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            if sum(nums) == k:
                return 1
            else:
                return 0
        prefix_dict = {0:1}
        prefix = 0
        re = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - k in prefix_dict:
                re += prefix_dict[prefix - k]
            if prefix in prefix_dict:
                prefix_dict[prefix] += 1
            else:
                prefix_dict[prefix] = 1


        return re









