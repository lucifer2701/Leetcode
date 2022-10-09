from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x=Counter(nums)
        n=len(nums)
        for ele in x:
            if x[ele]>n//2:
                return ele
            