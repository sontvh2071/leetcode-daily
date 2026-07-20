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
    
    # 1672. richest customer wealth
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = sum(accounts[0])
        for customer in accounts:
            if sum(customer) > maxWealth:
                maxWealth = sum(customer)
        return maxWealth
    
    # 485 max consecutive ones
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCon = 0
        currentCon = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currentCon += 1
                maxCon = max(currentCon, maxCon)
            else:
                currentCon = 0
        
        return maxCon
    
    # 414 third maximum number
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        
        m = [float('-inf'), float('-inf'), float('-inf')]
        for i in range(len(nums)):
            if nums[i] > m[0]:
                m[2] = m[1]
                m[1] = m[0]
                m[0] = nums[i]
            elif nums[i] > m[1]:
                m[2] = m[1]
                m[1] = nums[i]
            elif nums[i] > m[2]:
                m[2] = nums[i]
        
        return m[2]
            
            
        