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
    
    # 1480 - running sum of 1d array problem
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        runningSum.append(nums[0])
        
        for i in range(1, len(nums)):
            runningSum.append(runningSum[i -1] + nums[i])
            
        
        return runningSum
    
    # 1431 - kids with the greatest number of candies problem
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        result = [False] * len(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest:
                result[i] = True

        return result
