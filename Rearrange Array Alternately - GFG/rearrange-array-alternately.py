#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        x=0;y=n-1
        m=arr[-1]+1
        for i in range(0,n,2):
            arr[i]+=(arr[y]%m)*m
            y-=1
        for j in range(1,n,2):
            arr[j]+=(arr[x]%m)*m
            x+=1
        for k in range(n):
            arr[k]//=m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends