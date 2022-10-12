#User function Template for python3

class Solution:
    def smallestpositive(self, array, n): 
          
        array.sort()
        ans=1
        for i in range(n):
            if ans<array[i]:
                return ans
            else:
                ans = ans+array[i]
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.smallestpositive(array,n))


# } Driver Code Ends