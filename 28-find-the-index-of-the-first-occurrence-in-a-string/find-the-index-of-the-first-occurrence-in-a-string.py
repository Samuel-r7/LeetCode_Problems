class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)
        if h < n:
            return -1

        for i in range(h):
            if haystack[i:i+n] == needle:
                return i

        return -1
    