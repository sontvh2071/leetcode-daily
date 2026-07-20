from typing import List

class Solution:
    # 1 - two sum problem
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in pos:
                return [pos[needed], i]

            pos[num] = i
        
        return []