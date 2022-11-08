class Solution:
	def minDifference(self, arr, n):
		sum_ = sum(arr)
		attainable = [True] + [False] * sum_
		cumul_sum = 0
		for x in arr:
            for s in range(cumul_sum + 1)[::-1]: # reverse for in-place
                attainable[s + x] |= attainable[s]
            cumul_sum += x
        s = (sum_ + 1) // 2
        while not attainable[s]:
            s += 1
        return 2 * s - sum_


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends