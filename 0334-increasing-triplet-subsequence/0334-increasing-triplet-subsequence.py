class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first,second=inf,inf
        for ele in nums:
            if ele<first:
                first=ele
            elif ele<second and ele!=first:
                second=ele
            if ele>first and ele>second:
                return 1
        return 0