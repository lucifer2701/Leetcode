from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c=Counter(arr)
        x=c.values()
        if len(x)==len(set(x)):
            return 1
        return 0