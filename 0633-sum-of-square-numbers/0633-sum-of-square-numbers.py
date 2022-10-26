class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if (c <= 1): return True
        val = sqrt(c)
        if (val == int(val)): return True
        for a in range(1, int(sqrt(c))+1):
            val = sqrt(c - a*a)
            if (val == int(val)):
                print(val)
                return True
        return False