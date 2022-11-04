class Solution:
    def reverseVowels(self, s: str) -> str:
        d={'a':1,'e':1,'i':1,'o':1,'u':1}
        ans='';res=''
        for i in s:
            if i.lower() in d:
                ans+=i
        ans=ans[::-1]
        j=0
        for i in s:
            if i.lower() not in d:
                res+=i
            else:
                res+=ans[j]
                j+=1
        return res