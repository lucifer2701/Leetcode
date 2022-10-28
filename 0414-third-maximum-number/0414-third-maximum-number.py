class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n_set = set(nums)
        if len(n_set) < 3:
            return max(n_set)
        
        first, second, third = float('-inf'), float('-inf'), float('-inf')
        for n in n_set:
            if n > first:
                third, second, first = second, first, n
            elif n > second:
                third, second, = second, n
            elif n > third:
                third = n
        
        return third