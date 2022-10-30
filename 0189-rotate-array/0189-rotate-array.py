class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=len(nums)
        t=nums.copy()
        nums.clear()
        if x-k >= 0:
            t=t[x-k:]+t[:x-k]
        else:
            p=x-(k%x)
            t=t[p:]+t[:p]
        nums.extend(t)