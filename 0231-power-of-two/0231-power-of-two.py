class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return 0
        while n>1:
            if n%2==0:
                n=n//2
            else:
                return 0
        return 1