class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:    return 0
        if x==1 or x==2 or x==3 :    return 1
        if x==4 or x==5 or x==6 or x==7:    return 2
        for i in range(2,(x//2)+1):
            if x>=(i*i): pass
            else:   return i-1