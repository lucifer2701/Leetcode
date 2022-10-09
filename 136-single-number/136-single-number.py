from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=Counter(nums)
        for ele in x:
            if x[ele]==1:   return ele