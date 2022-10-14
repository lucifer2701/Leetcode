class Solution:
	def getSum(self, X, Y, Z):
		# code here
		dp1=[[[-1 for i in range(Z+1)]for i in range(Y+1)] for i in range(X+1)]
		dp2=[[[-1 for i in range(Z+1)]for i in range(Y+1)] for i in range(X+1)]
		ans=[0]
		mod=1000000007
		def count(i,j,k):
		    if i==0 and j==0 and k==0:
		        return 1
		    if i<0 or j<0 or k<0:
		        return 0
		    if dp2[i][j][k]!=-1:
		        return dp2[i][j][k]
		    dp2[i][j][k]=0
		    res=0
		    res+=count(i-1,j,k)+count(i,j-1,k)+count(i,j,k-1)
		    dp2[i][j][k]=res
		    return res
		def solve(i,j,k):
		    if i<0 or j<0 or k<0:
		        return 0
		    if i==0 and j==0 and k==0:
		        return 0
		    if dp1[i][j][k]!=-1:
		        return dp1[i][j][k]
		    dp1[i][j][k]=0
		    res=0
		    res+=solve(i-1,j,k)*10+count(i-1,j,k)*4
		    res+=solve(i,j-1,k)*10+count(i,j-1,k)*5
		    res+=solve(i,j,k-1)*10+count(i,j,k-1)*6
		    dp1[i][j][k]=res
		    ans[0]+=res
		    return res
		solve(X,Y,Z) 
		return (ans[0])%mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		X,Y,Z = map(int,input().split())
		ob = Solution()
		ans = ob.getSum(X,Y,Z)
		print(ans)
# } Driver Code Ends