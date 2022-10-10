from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        x=Counter(nums)
        y=[0,1,2]
        ans=[]
        nums.clear()
        for ele in y:
            for i in range(x[ele]):
                nums.append(ele)