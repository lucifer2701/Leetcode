
class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        d={}
        for i in range(N):
            if A[i] in d:
                d[A[i]]+=1
            else:   d[A[i]]=1
            if B[i] in d:
                d[B[i]]-=1
            else:   d[B[i]]=-1
        if max(d.values())==0 and min(d.values())==0:
            return 1
        return 0
        #return: True or False
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends