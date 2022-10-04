class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        o=['(','[','{']
        c=[')',']','}']
        for i in range(len(s)):
            if s[i] in o:
                stack.append(s[i])
            elif s[i] in c:
                x=c.index(s[i])
                y=100
                if len(stack)!=0:
                    y=o.index(stack[-1])
                if x==y:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        