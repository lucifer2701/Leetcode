class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        s=list(s)
        for i in range(len(s)):
            if s[i]=='(':
                stack.append('(')
            elif s[i]==')':
                if len(stack)>0:
                    stack.pop(0)
                else:
                    s[i]=""
        x=len(stack)
        i=len(s)-1
        while x!=0:
            if s[i]=='(':
                s[i]=""
                x-=1   
            i-=1
        return "".join(s)          