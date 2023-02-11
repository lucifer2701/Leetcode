from typing import List


class Solution:
    def getMinimumDays(self, N : int, S : str, P : List[int]) -> int:
        # code here
        s=list(S);d=0;j=0
        for i in range(N-1):
            if s[i]!="?" and s[i]==s[i+1]:
                while s[i]==s[i+1]:
                    s[P[d]]="?"
                    d+=1
        return d




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
        
        
        S = (input())
        
        
        P=IntArray().Input(N)
        
        obj = Solution()
        res = obj.getMinimumDays(N, S, P)
        
        print(res)
        

# } Driver Code Ends