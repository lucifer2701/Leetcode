#User function Template for python3



def maxArea(A,le):
    ans=float('-inf')
    i=0;j=le-1
    if le==1:
        return 0
    while i<j:
        ans=max(ans,(j-i)*min(A[i],A[j]))
        if (A[i]<A[j]):
            i+=1
        else:
            j-=1
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends