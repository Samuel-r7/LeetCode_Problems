class Solution:
    def frequencySort(self, s: str) -> str:
        a = list(s)
        count1 = Counter(a)

        sorted_arr = sorted(a, key=lambda x: (-count1[x], x))

        return "".join(sorted_arr)
        