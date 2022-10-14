class Solution:

    def minCount(self, l, n):

        # code here

        l.insert(0,float('inf'))

        l.insert(0,-float('inf'))

       

        dp=[[[-1 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]

        def ss(i,j,k):

            if k-2>=n:

                return(0)

            if dp[i][j-1][k-2]!=-1:

                return(dp[i][j-1][k-2])

           

            if l[k]>l[i]:

                dp[i][j-1][k-2]=ss(k,j,k+1)

           

            if l[k]<l[j]:

                if dp[i][j-1][k-2]==-1:

                    dp[i][j-1][k-2]=ss(i,k,k+1)

                else:

                    dp[i][j-1][k-2]=min(dp[i][j-1][k-2], ss(i,k,k+1))

            if dp[i][j-1][k-2]==-1:

                dp[i][j-1][k-2]=ss(i,j,k+1)+1

            else:

                dp[i][j-1][k-2]=min(dp[i][j-1][k-2], ss(i,j,k+1)+1)

           

            return(dp[i][j-1][k-2])

       

        return(ss(0,1,2))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCount(arr,n)
		print(ans)

# } Driver Code Ends