class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p,q,r=nums.count(0),nums.count(1),nums.count(2)
        nums[:p]=[0]*p
        nums[p:p+q]=[1]*q
        nums[p+q:p+q+r]=[2]*r        