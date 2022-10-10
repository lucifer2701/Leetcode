class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n=len(palindrome)
        s='abcdefghijklmnopqrstuvwxyz'
        i=0
        a=list(palindrome)
        a=set(a)
        a=list(a)
        if n==1:    return ''
        if len(a)==1 and s.index(a[0])==0:
            palindrome=palindrome[:n-1]+'b'
            return palindrome
        elif len(a)==1 and s.index(a[0])>0:
            palindrome=palindrome.replace(a[0],'a',1)
            return palindrome
        while n>0:
            x=palindrome[i]
            y=s.index(x)
            if y==0:
                i+=1
            elif i==n//2 and n%2==1 :
                palindrome=palindrome[:n-1]+'b'
                return palindrome
                
            else:
                palindrome=palindrome.replace(x,'a',1)
                return palindrome
                