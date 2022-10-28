from collections import Counter
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        d=Counter(nums)
        z=sorted(d.keys())
        a=0
        for i in range(len(z)-1,-1,-1):
            a+=d[z[i]]
            if a>=k:
                return z[i]
            
        