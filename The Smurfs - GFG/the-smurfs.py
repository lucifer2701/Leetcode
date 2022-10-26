#User function Template for python3

class Solution:
    def minFind(self, n, a):
        # code here
        li=[0,0,0]
        for ele in a:
            if ele=='R':
                li[0]+=1
            elif ele=='G':
                li[1]+=1
            else:
                li[2]+=1
        if li[0]==n or li[1]==n or li[2]==n:
            return n
        elif (li[0]%2==0 and li[1]%2==0 and li[2]%2==0) or (li[0]%2==1 and li[1]%2==1 and li[2]%2==1) :
            return 2
        else:
            return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        
        ob = Solution()
        print(ob.minFind(n, a))
# } Driver Code Ends