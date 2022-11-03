class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1=len(s1)
        for i in range(0,len(s2)-len1+1):
            dic=s2[i:len1+i]
            #from collections import Counter
            #s='asif'
            #print(Counter(s)) ==> Counter({'a': 1, 's': 1, 'i': 1, 'f': 1})
            if Counter(dic)==Counter(s1):
                return True
        return False