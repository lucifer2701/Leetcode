from typing import List


class Solution:
    def totalCuts(self, n : int, K : int, A : List[int]) -> int:
        # code here
        mini=float('inf');maxi=0
        mi=[];ma=[]
        for i in range(n-1):
            maxi=max(maxi,A[i])
            ma.append(maxi)
        for i in range(n-1,0,-1):
            mini=min(mini,A[i])
            mi.append(mini)
        mi=mi[::-1];c=0
        for i in range(n-1):
            if mi[i]+ma[i]>=K:
                c+=1
        return c


#{ 
 # Driver Code Starts
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
        
        N = int(input())
        
        
        K = int(input())
        
        
        A=IntArray().Input(N)
        
        obj = Solution()
        res = obj.totalCuts(N,K,A)
        
        print(res)
        

# } Driver Code Ends