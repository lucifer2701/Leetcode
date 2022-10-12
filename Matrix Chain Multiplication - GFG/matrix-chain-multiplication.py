#User function Template for python3

from math import inf
class Solution:
    def matrixMultiplication(self, n, x):
        dp={}
        def f(i,j):
            if j-i<=1:return 0
            if (i,j) in dp:return dp[i,j]
            ans=inf
            for k in range(i+1,j):
                ans=min(ans,f(i,k)+f(k,j)+x[i]*x[j]*x[k])
            dp[i,j]=ans
            return ans
        return f(0,n-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends