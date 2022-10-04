class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return x
        if n == 0:
            return 1

        if n < 0:
            return self.myPow(1 / x, -n)
        if not n % 2:
            return self.myPow(x * x, n // 2)

        return x * self.myPow(x * x, n // 2)