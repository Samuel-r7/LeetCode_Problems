class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_index = nums.index(max_val)

        for i in range(len(nums)):
            if i != max_index and 2*nums[i] > max_val:
                return -1
        
        return max_index
        