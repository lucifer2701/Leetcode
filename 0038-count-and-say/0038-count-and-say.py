class Solution:
    def countAndSay(self, n: int) -> str:
        count = [str(i) for i in range(0,10)]
        
        if n==1:
            return "1"
        i=1
        s="1"
        while(i<n):
            s2=""
            curr=s[0]
            c=0
            for ch in s:
                if curr==ch:
                    c+=1
                else:
                    s2+=str(c)+curr
                    curr = ch
                    c=1
            s2+=str(c)+curr
            s=s2
            
            i+=1
        return s2