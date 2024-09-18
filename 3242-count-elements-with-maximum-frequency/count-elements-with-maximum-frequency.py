from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        freq_count = Counter(nums)
        max_value = max(freq_count.values())
        count = 0
        for key, value in freq_count.items():
            if value == max_value:
                count += value
        return count