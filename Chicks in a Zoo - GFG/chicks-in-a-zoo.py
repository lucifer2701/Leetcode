#User function Template for python3

class Solution:
	def NoOfChicks(self, N):
		a=1
		li=[1]
		for i in range(1,N):
		    if i>=6:
		        a-=li[0]
		        li.pop(0)
		    li.append(2*a)
		    a+=2*a
		        
        return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		obj = Solution()
		ans = obj.NoOfChicks(N)
		print(ans)

# } Driver Code Ends