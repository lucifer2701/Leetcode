class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=[];c=0
        for ele in nums:
            if ele==1:
                c+=1
            if ele==0:
                c=0
            ans.append(c)
        return max(ans)