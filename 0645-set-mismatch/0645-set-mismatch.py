class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans=[];t=[]
        dic={}
        for i in range(1,len(nums)+1):
            if nums[i-1] in dic:
                dic[nums[i-1]]+=1
            else:   dic[nums[i-1]]=1
        for i in range(1,len(nums)+1):
            if i not in dic:    ans.append(i)
            elif dic[i]>1:  t.append(i)
        return t+ans