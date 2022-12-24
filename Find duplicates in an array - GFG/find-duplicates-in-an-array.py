from collections import Counter
class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	d=Counter(arr)
    	l=[i for i in d if d[i]>1]
    	if len(l)==0:
    	    return [-1]
    	return sorted(l)


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends