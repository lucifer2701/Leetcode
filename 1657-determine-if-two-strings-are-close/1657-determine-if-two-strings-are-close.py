from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1=Counter(word1);d2=Counter(word2)
        t1=[];t2=[]
        if len(word1)!=len(word2) and len(d1)!=len(d2):    return 0
        for ele in d2:
            if ele in d1 and d1[ele]==d2[ele]:
                pass
            elif ele in d1:
                t1.append(d1[ele])
                t2.append(d2[ele])
            else:
                return 0
        if len(t1)!=len(t2):
            return 0
        t1.sort();t2.sort()
        if t1!=t2:
            return 0
        return 1
        
                