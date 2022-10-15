class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        li=list(s.split(" "))
        if len(pattern)!=len(li):   return 0
        return len(set(pattern)) == len(set(li)) == len(set(zip(pattern,li)))
        