class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        l = len(s)
        idx=0

        for i in range(l-1,-1,-1):
            if s[i] == ' ':
                idx = i+1
                break
        return len(s[idx:l])
                
        