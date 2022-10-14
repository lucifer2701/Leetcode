#User function Template for python3
class Solution:
   def nextHappy (self, N):
       # code here
       def check(N):
           if N==1 or N==7:
               return True
           sm,n=N,N
           while sm>9:
               sm=0
               while n:
                   re=n%10
                   sm+=re*re
                   n//=10
               if sm==1:
                   return True
               n=sm
           if sm==7:
               return True
           return False
       
       i=N+1
       while True:
           if check(i):return i
           i+=1

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())

        ob = Solution()
        print(ob.nextHappy(N))
# } Driver Code Ends