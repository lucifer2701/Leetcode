class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        l = len(s)
        signo = 1
        i= 0
        while i < l:
            char = s[i]
            if char == '+':
                signo = 1
            elif char == '-':
                signo = -1
            elif char == '(':
                stack.append([signo, 0])
                signo = 1
            elif char == ')':
                sg, val = stack.pop(-1)
                if stack:
                    stack[-1][1] += sg*val 
                else: 
                    stack.append([1, sg*val])
            elif char == ' ':
                i += 1
                continue
            else: 
                number = ''
                while i< l and s[i].isnumeric():
                    number += s[i]
                    i += 1
                if stack:
                    stack[-1][1] += signo*int(number)
                else:
                    stack.append([1, signo*int(number)])
                continue
            i += 1
        return sum([sg*val for sg, val in stack])