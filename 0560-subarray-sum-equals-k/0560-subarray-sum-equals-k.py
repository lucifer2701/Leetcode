class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        hashmap=dict()
        temp=0
        hashmap[0]=1
        for i in nums:
            temp+=i
            if temp-k in hashmap:
                res+=hashmap[temp-k]
            if temp not in hashmap:
                hashmap[temp]=1
            else:
                hashmap[temp]+=1
                
        return res