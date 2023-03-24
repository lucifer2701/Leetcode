#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from collections import Counter
class Solution:
    def removeReverse(self, S): 
        #code here
        c = Counter(S) 
        f, r = 0, len(S)-1
        fv, rv = '', '' 
        control = True
        count = 0
        
        while f <= r : 
            if control : 
                if c[S[f]] > 1 : 
                    control = False 
                    count += 1
                    c[S[f]] -= 1
                else : 
                    fv += S[f] 
                f += 1 
            else : 
                if c[S[r]] > 1 : 
                    control = True 
                    count += 1
                    c[S[r]] -= 1
                else : 
                    rv += S[r] 
                r -= 1 
        
        ans = fv + rv[::-1] 
        
        if count%2 == 0 :
            return ans
        else : 
            return ans[::-1]
                
                
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.removeReverse(S)
        print(ans)


# } Driver Code Ends