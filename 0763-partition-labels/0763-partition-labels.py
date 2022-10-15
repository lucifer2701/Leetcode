from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        x=Counter(s)
        li=[]
        n=len(s)
        i,j=0,1
        c=0
        while i<n:
            y=Counter(s[i:j])
            for ele in y:
                if y[ele]==x[ele]:
                    c+=1
                else:
                    c=0
                    break
                if c==len(y):
                    li.append(j-i)
                    i=j
                    c=0
            j+=1
        return li
                