#User function Template for python3

class Solution:
    def maxFrequency(self, S):
       a=S[0]
       for i in range(len(S)-1,-1,-1):
           if S[i:]==S[0:len(S)-i]:
               a=S[i:]
               break
       return(S.count(a))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        Str = input()
        obj = Solution()

        print(obj.maxFrequency(Str))

# } Driver Code Ends