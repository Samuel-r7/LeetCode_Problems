class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = 0
        c2 = 0

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                c1+=1
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                c2+=1
        
        return [c1,c2]

        