#User function Template for python3

class Solution:
	def countTriplets(self, A):
	    N = len(A)
	    if N<3: return 0
	    rh = [0] * (N-1) # count of right-side numbers which are bigger
	    rh[N-2] = 1 if A[N-2]<A[N-1] else 0
	    rh[N-3] = (1 if A[N-3]<A[N-2] else 0) + (1 if A[N-3]<A[N-1] else 0)
	    ans = 0
	
	    for i in range(N-3, -1, -1):
	        rh[i] = 1 if A[i]<A[N-1] else 0
	        for j in range(i+1, N-1):
	            if A[i]>=A[j]: continue
	            rh[i]+=1
	            ans += rh[j]
	    return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int,input().split()))
		ob = Solution()
		ans = ob.countTriplets(nums)
		print(ans)

# } Driver Code Ends