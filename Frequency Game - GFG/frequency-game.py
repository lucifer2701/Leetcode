#User function Template for python3

from collections import Counter
def LargButMinFreq(arr,n):
    #code here
    c=Counter(arr)
    x=min(c.values())
    ans=0
    for i in c:
        if c[i]==x:
            ans=max(i,ans)
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
#Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
# } Driver Code Ends