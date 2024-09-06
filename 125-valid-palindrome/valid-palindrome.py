class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a =""
        for i in s:
            if i.isalnum():
                a+= str(i)     
        b = a[::-1]  
        if a==b:
            return True
        else:
            return False