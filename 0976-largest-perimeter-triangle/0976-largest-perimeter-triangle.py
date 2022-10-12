class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True) 
        for i in range(len(nums) -2) :
            j=i+1
            k=j+1
            if nums[i]<nums[j]+nums[k] :
                return nums[i]+nums[j]+nums[k]
        return 0
        