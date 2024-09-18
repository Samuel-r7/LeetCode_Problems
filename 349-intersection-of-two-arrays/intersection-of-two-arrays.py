class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        set1 = set(nums1)
        # set2 =set(nums2)
        # intersection = set1 & set2
        # return intersection
        res=[]
        for num in nums2:
            if num in set1:
                res.append(num)

        return set(res)
