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
    
    # 1470 - shuffle the array problem
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled = [0] * (2 * n)
        shuffled[0] = nums[0]
        shuffled[1] = nums[n]
        

        for i in range(1, n):
            shuffled[i * 2] = nums[i]
            shuffled[i * 2 + 1] = nums[i + n]
            
        return shuffled