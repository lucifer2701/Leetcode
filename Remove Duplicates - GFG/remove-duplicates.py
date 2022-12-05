#User function Template for python3
class Solution:
	def removeDups(self, S):
		# code here
		d={};ans=""
		for i in S:
		    if i not in d:
		        ans+=i
		        d[i]=1
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeDups(s)
		
		print(answer)


# } Driver Code Ends