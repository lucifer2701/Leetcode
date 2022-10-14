from typing import List
from math import inf
from heapq import heappush as push, heappop as pop
class Solution:
    def maximumDistance(self, n : int, e : int, src : int, edges : List[List[int]]) -> List[int]:
        x=[[] for i in range(n)]
        dp=[None for i in range(n)]
        dp[src]=0
        for a,b,c in edges:
            x[b].append((a,c))
        def f(i):
            if i==src:return 0
            if dp[i]!=None:return dp[i]
            ans=-inf
            for j,k in x[i]:
                ans=max(ans,k+f(j))
            dp[i]=ans
            return ans
        for i in range(n):
            f(i)
        return ['INF' if i==-inf else i for i in dp]


#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        v = int(input())
        
        
        e = int(input())
        
        
        src = int(input())
        
        
        edges=IntMatrix().Input(e, e)
        
        obj = Solution()
        res = obj.maximumDistance(v, e, src, edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends