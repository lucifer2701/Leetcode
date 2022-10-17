class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li=list(s.split())
        return len(li[-1])