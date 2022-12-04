class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        s=sum(nums);x=0;temp=float('inf');n=len(nums)
        for i in range(1,n+1):
            x+=nums[i-1]
            s-=nums[i-1]
            if i==n:
                t=(x//i)
            else:
                t=abs((x//i)-(s//(n-i)))
            test=temp
            temp=min(temp,t)
            if temp!=test:
                ans=i-1
        return ans