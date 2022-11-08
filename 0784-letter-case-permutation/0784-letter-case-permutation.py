class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        arr = []
        def bt(start, curr):
            if len(curr) == len(s):
                arr.append(''.join(curr))
                return
            if s[start].isalpha():
                bt(start+1, curr+[s[start].lower()])
                bt(start+1, curr+[s[start].upper()])
            else:
                bt(start+1, curr+[s[start]])
        
        bt(0, [])
        return arr