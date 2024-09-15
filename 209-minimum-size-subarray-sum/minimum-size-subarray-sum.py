class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        start = 0
        min_len = float('inf')
        cur_sum = 0

        for end in range(len(nums)):
            cur_sum += nums[end]

            while cur_sum >= target:
                no_of_ele_in_window = end - start +1
                min_len = min(min_len,no_of_ele_in_window)
                cur_sum -= nums[start]
                start+=1

        if min_len != float('inf'):
            return min_len
        else:
            return 0 
                
        