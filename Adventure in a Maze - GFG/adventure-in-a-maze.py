#User function Template for python3

class Solution:
	def FindWays(self, matrix):
		m, n = len(matrix), len(matrix[0])
		#dp = [[0 for _ in range(n)] for _ in range(m)]
		dp = [[0]*n for _ in range(m)]
		M=1000000007
		for i in range(m):
		    for j in range(n):
		        num = 1 if (i, j) == (0, 0) else 0
		        value = 0
		        if i > 0 and matrix[i-1][j] in [2, 3]:
		            value = max(value, dp[i-1][j][1])
		            num += dp[i-1][j][0]
		        if j > 0 and matrix[i][j-1] in [1, 3]:
		            value = max(value, dp[i][j-1][1])
		            num += dp[i][j-1][0]
		        if value == 0 and (i, j) != (0, 0):
		            dp[i][j] = num, 0
		        else:
		            dp[i][j] = num%M, (value + matrix[i][j])%M
		        
		return dp[m-1][n-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			cur = list(map(int, input().split()))
			matrix.append(cur)
		obj = Solution()
		ans = obj.FindWays(matrix)
		for _ in ans:
			print(_, end = " ")
		print()

# } Driver Code Ends