#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		arr=set(arr)
		arr=list(arr)
		arr.sort()
		n=len(arr)
		if n<2:
		    return -1
		return arr[n-2]
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends