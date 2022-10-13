#User function template for Python

class Solution:	
	def buzzTime(self, N, M, L, H, A):
		# code here
		def speed(H, A, T):
		    return H+A*T
		def finalSpeed(T):
		    tot = 0
		    for i in range(N):
		        s = speed(H[i],A[i],T)
		        if s >= L:
		            tot += s
		    return tot>=M
		low = 0
		high = 10**9
		while low < high:
		    mid = (low+high) //2
		    if finalSpeed(mid):
		        high = mid
		    else:
		        low = mid + 1
		return high
		# code here


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M, L = [int(x) for x in input().split()]
        H = [0 for x in range(N)]
        A = [0 for x in range(N)]
        for i in range(N):
            H[i], A[i] = [int(y) for y in input().split()]
        ob = Solution()
        print(ob.buzzTime(N, M, L, H, A))

# } Driver Code Ends