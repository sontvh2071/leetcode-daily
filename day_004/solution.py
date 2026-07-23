import heapq
from typing import List, Tuple


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
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        m = {}
        for task in tasks:
            m[task] = m.get(task, 0) + 1
        
        pq = []
        for val, count in m.items():
            heapq.heappush(pq, (-count, (val, -n - 1)))
        
        return self.solve(pq, 0, n)
            
    def solve(self, items: List[Tuple[int, Tuple[int, int]]], t: int, k: int) -> int:
        pq = []
        while items:            
            item = heapq.heappop(items)
            count = item[0]
            val = item[1][0]
            quota = item[1][1]
            
            if t > item[1][1] + k:
                count += 1
                quota = t
            else:
                heapq.heappush(pq, item)
                continue
                
            if count < 0:
                heapq.heappush(pq, (count, (val, quota)))
                

            t += 1

            
        if len(pq) == 0:
            return t    

        return self.solve(pq, t, k)

if __name__ == "__main__":
    s = Solution()
    print(s.leastInterval(["A","A","A","B","B","B"], 2))

            
            
            
        