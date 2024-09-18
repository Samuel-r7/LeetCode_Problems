class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        a = []
        for word in s.split():
            try:
                a.append(int(word))
            except ValueError:
                pass
        
        for i in range(1, len(a)):
            if a[i] <= a[i - 1]:
                return False

        return True
