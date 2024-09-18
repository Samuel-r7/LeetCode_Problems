class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        count =0
        for key, freq in count1.items():
            if freq ==1 and count2.get(key,0) == 1:
                count += 1
        return count

 
        