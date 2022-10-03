class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n=len(colors)
        t=neededTime
        ans=0
        for i in range(1,n):
            if colors[i]==colors[i-1]:
                ans+=min(t[i],t[i-1])
                t[i]=max(t[i],t[i-1])
        return ans