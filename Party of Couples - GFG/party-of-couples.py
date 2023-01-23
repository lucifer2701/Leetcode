#User function Template for python3

class Solution:
    def findSingle(self, N, arr):
        d={}
        for ele in arr:
            if ele not in d:
                d[ele]=1
            else:
                d[ele]+=1
        for ele in d:
            if d[ele]%2==1:
                return ele
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.findSingle(N, arr))

# } Driver Code Ends