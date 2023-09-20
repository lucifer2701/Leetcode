#User function Template for python3

class Solution:
    def rotate(self, N, D):
        # code here
        s=bin(N).replace("0b","")
        n=len(s)
        D=D%16
        s1="".join(["0"]*(16-n))+s
        t1=s1[D:]+s1[:D]
        t2=s1[16-D:]+s1[:16-D]
        return int(t1,2),int(t2,2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
# } Driver Code Ends