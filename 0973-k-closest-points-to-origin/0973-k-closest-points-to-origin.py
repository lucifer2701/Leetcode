class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d={}
        for ele in points:
            x=(ele[0]**2) + (ele[1]**2)
            if x not in d:
                d[x]=[]
            d[x].append(ele)
        ans=[]
        for i in sorted(d.keys()):
            z=d[i]
            ans.extend(z[:k])
            k-=len(d[i])
        return ans