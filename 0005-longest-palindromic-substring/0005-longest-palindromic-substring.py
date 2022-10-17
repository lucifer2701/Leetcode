class Solution:
    def longestPalindrome(self, s: str) -> str:
        x=len(s)
        ans=s[0]
        if s==s[::-1]:
            ans=s
            return ans
        for i in range(x-1):
            for j in range(x-1,i,-1):
                temp=s[i:j+1]
                if temp==temp[::-1] and len(temp)>len(ans):
                    ans=temp
        return ans
                
                