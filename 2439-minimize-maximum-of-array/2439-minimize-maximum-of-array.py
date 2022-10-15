class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        pre_sum = [0] * len(nums)
        pre_sum[0] = nums[0]
        avg_ceil = [0] * len(nums)
        avg_ceil[0] = nums[0]
        for i in range(1, len(nums)):
            pre_sum[i] = pre_sum[i - 1] + nums[i]
            avg_ceil[i] = math.ceil(pre_sum[i] / (i + 1))
        
        ans = avg_ceil[0]
        for i in range(1, len(nums)):
            if nums[i] > ans:
                ans = max(ans, avg_ceil[i])
        return ans