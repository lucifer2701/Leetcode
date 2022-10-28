class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        l=[]
        for ele in nums:
            if ele%2==0:
                l.append(ele)
        m=-1
        if len(l)==0:   return m
        x=collections.Counter(l)
        for ele in x:
            m=max(m,x[ele])
        ans=[]
        for ele in x:
            if m==x[ele]:
                ans.append(ele)
        return min(ans)
