class Solution:
    def addBinary(self, a: str, b: str) -> str:
        temp = int(a,2)
        temp2 = int(b,2)
        sum=temp+temp2
        ans=bin(sum)
        return ans[2: ]
        