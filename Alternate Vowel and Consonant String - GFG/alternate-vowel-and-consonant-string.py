#User function Template for python3
class Solution:
    def rearrange(self, S, N):
        # code here
        s={'a','e','i','o','u'}
        Sa=list(S)
        Sa.sort()
        vc=0;cc=0
        dv=[];dc=[]
        ans=""
        for i in Sa:
            if i in s:
                vc+=1
                dv.append(i)
            else:
                cc+=1
                dc.append(i)
        if abs(vc-cc)>1:
            return -1
        p=0
        if vc==cc:
            if dc[0]>dv[0]:
                while vc>p:
                    ans+=dv[p]+dc[p]
                    p+=1
            else:
                while vc>p:
                    ans+=dc[p]+dv[p]
                    p+=1
            return ans
        elif vc>cc:
            ans+=dv[0]
            while cc>p:
                ans+=dc[p]+dv[p+1]
                p+=1
            return ans
        else:
            ans+=dc[0]
            while vc>p:
                ans+=dv[p]+dc[p+1]
                p+=1
            return ans
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N = int(input().strip())
        S = input().strip()
        ob=Solution()
        ans=ob.rearrange(S, N)
        print(ans)
# } Driver Code Ends