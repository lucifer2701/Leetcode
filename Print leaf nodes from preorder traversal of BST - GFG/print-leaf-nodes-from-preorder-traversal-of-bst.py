#User function Template for python3
class Solution:
	def leafNodes(self, arr, N):
		stack=[];res=[]
		for ele in arr:
		    if stack and stack[-1]<ele:
		        prev=stack.pop()
		        if stack and stack[-1]<ele:
		            res.append(prev)
		            while stack and stack[-1]<ele:
		                stack.pop()
		    stack.append(ele)
	    res.append(stack[-1])
	    return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        ans = ob.leafNodes(arr,N)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
# } Driver Code Ends