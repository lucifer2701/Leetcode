class Solution:
    def frequencySort(self, s: str) -> str:
        z=''.join(x for x,_ in sorted(Counter(s).items(),key=lambda y:-y[1])[:])
        c=collections.Counter(s)
        ans=''
        for ele in z:
            ans+=ele*c[ele]
        return ans