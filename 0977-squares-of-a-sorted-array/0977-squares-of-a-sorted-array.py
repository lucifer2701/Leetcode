class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            i=i*i
            ans.append(i)
        ans.sort()
        return ans