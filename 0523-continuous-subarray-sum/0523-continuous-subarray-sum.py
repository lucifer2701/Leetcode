class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders={0:-1}
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            r=s%k
            if r not in remainders:
                remainders[r]=i
            elif i-remainders[r]>=2:
                return 1
        return 0