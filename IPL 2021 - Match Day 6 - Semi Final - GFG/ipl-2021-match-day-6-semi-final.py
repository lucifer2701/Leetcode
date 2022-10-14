
class Solution:
    def fillarray(self, s, a):
        a[0]=0
        for i in range(1,len(s)):
            series=a[i-1]
            while(series):
                if(s[series]==s[i]):
                    a[i]=series+1
                    break
                series=a[series-1]
            if(series==0):
                a[i]=(int(s[i]==s[0]))
        return a*1
        
    def compress(self, s):
        a=[0]*len(s)
        a = self.fillarray(s, a)
        shortened=[]
        n=len(s)
        i=n-1
        while(i>0):
            if(i%2==0):
                shortened.append(s[i])
                i-=1
                continue
            star_here=False
            suffix=a[i]
            substrlen=i+1
            if(suffix*2>=substrlen):
                if(substrlen%(substrlen-suffix)==0):
                    if((substrlen/(substrlen-suffix))%2==0):
                        star_here=True
            if(star_here==True):
                shortened.append('*')
                i=(i//2)+1
            else:
                shortened.append(s[i])
            i=i-1
        ret=""
        ret=ret+s[0]
        n=len(shortened)
        while(n):
            ret=ret+shortened[n-1]
            shortened.pop()
            n=n-1
        ans=ret
        return ans
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())    
for _ in range(0,t):
    s=input()
    obj = Solution();
    ans=obj.compress(s)
    print(ans)

# } Driver Code Ends