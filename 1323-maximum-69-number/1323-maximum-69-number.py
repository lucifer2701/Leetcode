from collections import Counter
class Solution:
    def maximum69Number (self, num: int) -> int:
        x=str(num)
        t=Counter(x)
        if '6' not in t:
            return num
        x=x.replace('6','9',1)
        x=int(x)
        return x