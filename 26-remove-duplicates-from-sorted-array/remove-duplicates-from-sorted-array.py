class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # j = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i-1]:
        #         nums[j] = nums[i]
        #         j +=1
        # return j

        s = set(nums)
        nums.clear()
        for i in s:
           nums.append(i)
        nums.sort()
        return len(nums)
        
        
        # nums[:] = list(set(nums))    Does not Work
        # return len(nums)