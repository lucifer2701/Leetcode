#User function Template for python3

class Solution:
    def maxTripletProduct (self, arr,  n): 
        #Complete the function
        mx1=max(arr);arr.remove(mx1)
        mx2=max(arr);arr.remove(mx2)
        mx3=max(arr);arr.remove(mx3)
        if len(arr)==0:
            return mx1*mx2*mx3
        if len(arr)>0:
            mi1=min(arr)
            arr.remove(mi1)
        else:
            mi1=mx3
        if len(arr)>0:
            mi2=min(arr)
            arr.remove(mi2)
        else:
            mi2=mx3
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