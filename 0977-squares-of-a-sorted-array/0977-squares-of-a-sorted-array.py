class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            i=i*i
            ans.append(i)
        x=min(ans)
        a=ans.index(x)
        if a==0:
            return ans
        s=ans[:a]
        s.reverse()
        t=ans[a:]
        res=[]
        while len(s)>0 or len(t)>0:
            if len(s)>0 and len(t)>0:
                if s[0]<t[0]:
                    res.append(s.pop(0))
                elif s[0]>t[0]:
                    res.append(t.pop(0))
                else:
                    res.append(s.pop(0))
                    res.append(t.pop(0))
            else:
                if len(s)==0 and len(t)==0:
                    break
                if len(s)==0 and len(t)>0:
                    res.append(t.pop(0))
                if len(t)==0 and len(s)>0:
                    res.append(s.pop(0))
        return res