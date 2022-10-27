#User function Template for python3

class Solution:
	def NthTerm(self, n):
	    x=1
	    mod=10**9+7
		for i in range(n):
		    x=(x*(i+1)%mod)+1
		return x


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.NthTerm(n)
		print(ans)

# } Driver Code Ends