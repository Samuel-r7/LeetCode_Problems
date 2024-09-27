class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        n=len(nums)
        
        if nums[0] != 0:
            return 0
        if nums[-1] !=n:
            return n
        
        for i in range(1,len(nums)):
            if nums[i] != i:
                return i
        
        # return 0
        
        
        
        
        
        
        
        
        
        
        # n =len(nums)
        # ans=0
        # for i in range(1,n+1):
        #     ans = ans^i
        # print(ans)
        # for num in nums:
        #     ans = ans^num
        # print(ans)
        # return ans

        

        