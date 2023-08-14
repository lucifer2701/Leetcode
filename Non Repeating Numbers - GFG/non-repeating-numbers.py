#User function Template for python3
from collections import Counter
class Solution:
	def singleNumber(self, nums):
		# Code here
		c=Counter(nums)
		ans=[]
		for i in c:
		    if c[i]==1:
		        ans.append(i)
		ans.sort()
		return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends