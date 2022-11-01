class Solution:
    def reverseWords(self, s: str) -> str:
        li=s.split()
        ans=""
        for i in range(len(li)):
            x=li[i][::-1]
            ans+=x+" "
        return ans[:len(ans)-1]