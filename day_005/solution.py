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
                