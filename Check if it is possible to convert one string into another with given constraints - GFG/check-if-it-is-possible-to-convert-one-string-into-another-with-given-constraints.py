class Solution:
    def isItPossible(sef, s, t, m, n):
        #code here
        i, j = 0, 0 
        
        while i < m and j < n : 
            #print(s[i], s[j], i, j)
            if s[i] == '#' : 
                i += 1 
                
            elif t[j] == '#' : 
                j += 1 
                
            elif s[i] == t[j] :
                if s[i] == 'A' and i >= j :
                    i += 1 
                    j += 1 
                elif s[i] == 'B' and i <= j : 
                    i += 1 
                    j += 1 
                else : 
                    return 0
            else : 
                return 0 
            
        while i < m : 
            if s[i] != '#' :
                return 0 
            else : 
                i += 1 
        
        while j < n : 
            if t[j] != '#' :
                return 0 
            else : 
                j += 1 
        
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S,T=input().split()
        ob=Solution()
        print(ob.isItPossible(S,T,len(S),len(T)))
# } Driver Code Ends