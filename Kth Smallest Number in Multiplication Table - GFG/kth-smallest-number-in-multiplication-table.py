class Solution(object):
    def findKthNumber(self, m, n, k):
        #Write your code here
        lo,hi = 0,m*n+1
        while lo<hi:
            mid = (lo+hi)//2
            val = 0
            for i in range(m):
                val+=min(n,(mid//(i+1)))
            if val>=k:
                hi = mid
            else:
                lo = mid+1
        return hi

#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    arr = list(map(int, input().split())) 
    ob = Solution()
    print(ob.findKthNumber(arr[0],arr[1], arr[2]))
# } Driver Code Ends