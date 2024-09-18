class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count1 = Counter(arr)
        
        distinct_elements =[]

        for key,value in count1.items():
            if value ==1:
                distinct_elements.append(key)

        if k<= len(distinct_elements):
            return distinct_elements[k-1]
        else:
            return ""
        


        