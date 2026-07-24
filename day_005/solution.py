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
    
    # 205 isomorphic strings
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            if dict_s.get(s[i], None) is None and dict_t.get(t[i], None) is None:
                dict_s[s[i]] = t[i]
                dict_t[t[i]] = s[i]
            
            elif dict_s.get(s[i], None) != t[i] and dict_t.get(t[i], None) != s[i]:
                return False
        
        return True
    
    # 594 longest harmonious subsequence
    def findLHS(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1
        
        max_len = 0
        for k in m.keys():
            if (k+1) in m:
                max_len = max(max_len, m[k] + m[k+1])
        
        return max_len

if __name__ == "__main__":
    solution = Solution()
    print(solution.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
                