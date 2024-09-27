class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums_set = list(set(nums))
        b= sorted(nums_set)

        if len(b) <3:
            return b[-1]
        else:
            return b[-3]
        