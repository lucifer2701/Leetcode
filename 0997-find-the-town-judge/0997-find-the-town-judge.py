from collections import Counter
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        l1=[];l2=[]
        if n==1:    return 1
        for i in range(len(trust)):
            l1.append(trust[i][0])
            l2.append(trust[i][1])
        l2=Counter(l2)
        x=0
        for ele in l2:
            if l2[ele]==n-1:
                x=ele
        if x!=0 and x not in l1:
            return x
        return -1
        
        