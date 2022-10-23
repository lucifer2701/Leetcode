from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans=[];t=[]
        dic=Counter(nums)
        for i in range(1,len(nums)+1):
            if i not in dic:    ans.append(i)
            elif dic[i]>1:  t.append(i)
        return t+ans