class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x for x,_ in sorted(Counter(nums).items(),key=lambda y:-y[1])[:k]]