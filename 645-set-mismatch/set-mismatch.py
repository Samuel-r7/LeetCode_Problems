class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0,0]
        nums.sort()
        for num in range(len(nums)-1):
            if nums[num] == nums[num+1]:
                res[0] = nums[num]  
                # print(res[0])
        
        n=len(nums)
        expected_sum = (n*(n+1))//2

        actual_sum = sum(nums)
        res[1] = expected_sum - (actual_sum - res[0]) 

        return res
