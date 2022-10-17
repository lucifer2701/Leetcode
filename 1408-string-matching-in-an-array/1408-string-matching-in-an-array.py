class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        total="_".join(words)
        for i in words:
            ocur=total.count(i)
            if(ocur>1):
                res.append(i)
        return res