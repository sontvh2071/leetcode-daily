from typing import List

class Solution:
    
    # 121
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        
        return max_profit
    
    # 349
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        s = set([])
        for num in nums1:
            m[num] = 1
        for num in nums2:
            if num in m:
                s.add(num)
        return list(s)
    
    # 202
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while(n != 1):
            if n in seen:
                return False
            
            seen.add(n)
            happy = 0
            while(n > 0):
                happy += (n % 10) ** 2
                n //= 10
            n = happy
            
        return True
    
    # 1207
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f = {}
        for num in arr:
            f[num] = f.get(num, 0) + 1
        return len(f.values()) == len(set(f.values()))

    
    