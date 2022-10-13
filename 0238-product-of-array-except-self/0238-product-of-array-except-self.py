class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro=1
        pro2=1
        for ele in nums:
            pro*=ele
            if ele!=0:
                pro2*=ele
        x=nums.count(0)
        for i in range(len(nums)):
            if nums[i]==0 and x==1:  nums[i]=pro2
            elif x>1:   nums[i]=0
            else:   nums[i]=pro//nums[i]
        return nums
        