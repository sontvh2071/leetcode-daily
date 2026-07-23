import heapq
from typing import List


class Solution:
    # 347 top K frequent elements
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 1 and len(nums) == 1:
            return nums
        
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1
        
        pq = []
        for val, count in m.items():
            heapq.heappush(pq, (-count, val))
            
        f = []
        while pq and k:
            e = heapq.heappop(pq)
            f.append(e[1])
            k -= 1
        
        return f
        