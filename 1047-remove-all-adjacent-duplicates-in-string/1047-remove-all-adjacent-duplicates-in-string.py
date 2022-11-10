class Solution:
    def removeDuplicates(self, s: str) -> str:
        j = 0
        ans = []
        while j < len(s):
            if len(ans) == 0:
                ans.append(s[j])
            elif ans[-1] == s[j]:
                ans.pop()
            else:
                ans.append(s[j])
            j += 1
        return "".join(ans)