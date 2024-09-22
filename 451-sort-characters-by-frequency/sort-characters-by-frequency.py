class Solution:
    def frequencySort(self, s: str) -> str:
        count1 = Counter(s)
        sorted_arr = sorted(s, key=lambda x: (-count1[x], x))
        return "".join(sorted_arr)
        