import itertools
from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        x=Counter(nums)
        for ele in x:
            if x[ele]>3:    x[ele]=3
        newlist=[]
        for ele in x:
            for i in range(x[ele]):
                newlist.append(ele)
        nums=newlist
        n=len(nums)
        li=[]
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    li.append([nums[i],nums[j],nums[k]])
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1
        ans=list(li for li,_ in itertools.groupby(li))
        finalans=[]
        for i in range(len(ans)):
            if ans[i] not in finalans:
                finalans.append(ans[i])
        return finalans