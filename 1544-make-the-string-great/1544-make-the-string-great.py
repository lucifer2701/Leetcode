class Solution:
    def makeGood(self, s: str) -> str:

        # Initialize a stack
        stack = []

        # Iterate through all character
        for c in s:

            # Check if the character on top of the stack is no longer good
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:

                # If yes, pair it with the current character and remove both of it
                stack.pop()
                continue

            # Else, add the current character onto the stack
            stack.append(c)

        return "".join(stack)