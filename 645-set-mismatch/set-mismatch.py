class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0,0]
        nums.sort()
        for num in range(len(nums)-1):
            if nums[num] == nums[num+1]:
                res[0] = nums[num]  
                print(res[0])

        expected_sum = sum(range(1, len(nums) + 1))
        print(expected_sum)
        actual_sum = sum(nums)
        print(actual_sum)
        res[1] = expected_sum - (actual_sum - res[0]) 

        return res
