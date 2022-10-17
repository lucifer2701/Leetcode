class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return 0
        given_num=x
        t=0
        while x!=0:
            n=x%10
            t=10*t+n
            x=x//10
        return given_num==t
        