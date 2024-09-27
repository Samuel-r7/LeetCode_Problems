class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # freq = Counter(nums)
        # return freq.most_common(1)[0][0]
        
        nums.sort()
        return nums[len(nums)//2]

        # freq ={}

        # for num in nums:
        #     if num in freq:
        #         freq[num] +=1
        #     else:
        #         freq[num] = 1
        # maj = max(freq, key = freq.get)
        # return maj