from typing import List


class Solution:
    # 219 contains duplicate II
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1 or k == 0:
            return False

        dict = {}
        i = 0
        while i < len(nums):
            if i > k:
                dict[nums[i - k - 1]] = False
            
            if dict.get(nums[i], False):
                return True
            
            dict[nums[i]] = True
            i += 1
            
        return False
            
        