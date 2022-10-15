class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        li1=list(s.split(" "))
        li2=[pattern[i] for i in range(len(pattern))]
        if len(li2)!=len(li1):   return 0
        mp=[]
        for i in range(len(li1)):
            temp=(li1[i],li2[i])
            mp.append(temp)
            temp=()
        return len(set(li1)) == len(set(li2)) == len(set(mp))
        