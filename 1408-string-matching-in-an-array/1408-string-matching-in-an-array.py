class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        x=dict()
        for ele in words:
            x[ele]=ele
        ans=[]
        for ele in words:
            for w in x:
                if ele in x[w] and ele!=w:
                    ans.append(ele)
        ans=set(ans)
        return list(ans)
                    
                