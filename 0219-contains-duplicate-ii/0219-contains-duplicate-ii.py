class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic and (i-dic[nums[i]])<=k:
                return 1
            else:
                dic[nums[i]]=i
        return 0