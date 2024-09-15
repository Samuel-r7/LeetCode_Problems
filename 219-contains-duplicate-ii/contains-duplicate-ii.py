class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        idx_map = {}

        for i,num in enumerate(nums):
            if num in idx_map:
                 if i - idx_map[num] <=k:
                    return True
            
            idx_map[num] = i
        
        return False
        