#User function Template for python3

class Solution:
    def maxTripletProduct (self, arr,  n): 
        #Complete the function
        arr.sort()
        mx1=arr[-1]
        mx2=arr[-2]
        mx3=arr[-3]
        mi1=arr[0]
        mi2=arr[1]
        ans=1
        if mx1<0:
            ans=mx1*mx2*mx3
        elif mx2*mx3<mi1*mi2:
            ans=mx1*mi1*mi2
        else:
            ans=mx1*mx2*mx3
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.maxTripletProduct(arr, n)
    print(res)
# } Driver Code Ends