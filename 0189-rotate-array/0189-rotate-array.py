class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=len(nums)-1
        for i in range(k):
            t=nums.pop()
            nums.insert(0,t)
        
        