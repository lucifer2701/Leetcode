#User function Template for python3

class Solution:
    def partitionArray(self,N,K,M,arr):
        
        arr.sort()
        
        dp = [False] * N
        for i, e in enumerate(arr[K-1:], start=K-1):
            n = i+1-k+1
            lo, hi = 0, n
            while lo < hi:
                mi = lo+(hi-lo)//2
                if arr[i] - arr[mi] <= M:
                    hi = mi
                else:
                    lo = mi+1
                    
            for j in range(lo, n):
                if j == 0 or dp[j-1]:
                    dp[i] = True
                    break

        return dp[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,k,m=map(int,input().split())
        arr=list(map(int,input().strip().split()))
        obj=Solution()
        ans=obj.partitionArray(n,k,m,arr)
        if ans:
            print('YES')
        else:
            print('NO')
# } Driver Code Ends