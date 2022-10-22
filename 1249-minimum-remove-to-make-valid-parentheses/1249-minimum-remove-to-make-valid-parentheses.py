class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        s=list(s)
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                if len(stack)>0:
                    stack.pop(0)
                else:
                    s[i]=""
        for ele in stack:
            s[ele]=""
        return "".join(s)          