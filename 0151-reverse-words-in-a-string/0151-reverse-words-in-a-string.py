class Solution:
    def reverseWords(self, s: str) -> str:
        x=list(s.split())
        x.reverse()
        ans=" ".join(x)
        return ans