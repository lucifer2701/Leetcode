class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d={}
        for ele in points:
            x=(ele[0]**2) + (ele[1]**2)
            if x not in d:
                d[x]=[]
            d[x].append(ele)
        z=[d[x] for x,_ in sorted(d.items())]
        ans=[]
        i=0
        while k>0:            
            ans+=z[i][:k]
            k-=len(z[i])
            i+=1
        return ans