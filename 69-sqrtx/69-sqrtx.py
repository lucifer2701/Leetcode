class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:    return 0
        if x==1:    return 1
        for i in range(x+1):
            if x>=(i*i): pass
            else:   return i-1