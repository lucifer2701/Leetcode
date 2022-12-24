#User function Template for python3

class Solution:
    def nthFibonacci(self, n):
        # code here
        a1=1;a2=1
        if n==1 or n==2:
            return a1
        for i in range(n-2):
            a2+=a1
            a1=a2-a1
        return a2%1000000007


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthFibonacci(n))
# } Driver Code Ends