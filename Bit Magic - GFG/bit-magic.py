from typing import List


class Solution:
    def bitMagic(self, n : int, arr : List[int]) -> int:
        # code here
        c=0;i=0;j=n-1
        while i<j:
            if arr[i]!=arr[j]:
                c+=1
            i+=1
            j-=1
        if c%2==0:
            return c//2
        else:
            return c//2+1



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
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.bitMagic(n, arr)
        
        print(res)
        

# } Driver Code Ends