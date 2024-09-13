class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # for i in range(len(nums)-1):
        #     for k in range(i+1,len(nums)):
        #         if nums[i] == nums[k]:
        #             return True
        #         else:
        #             False  ------------------------>>>>>>>TLE
        
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False


