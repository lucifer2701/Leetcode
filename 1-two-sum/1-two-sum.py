class Solution:
    def twoSum(self, nums, target) -> list:
        l=[]
        for i in range (len(nums)):
            l.append(target-nums[i])
        i=0
        while(i<len(nums)):
            if l[i] in nums:
                index_1=i
                index_2=nums.index(l[i])
                if index_1!=index_2 :
                    return index_1,index_2
                    break
                else: 
                    pass
            i+=1