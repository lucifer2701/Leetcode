class Solution:
    def outerTrees(self, trees):
        def cross(p1,p2,p3):
            return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])

        def construct(points):
            stack = []

            for i in points:
                while len(stack) >= 2 and cross(stack[-2],stack[-1],i) > 0:
                    stack.pop()
                stack.append(tuple(i))

            return stack

        trees.sort()

        lefttoright = construct(trees)
        righttoleft = construct(trees[::-1])

        return list(set(lefttoright + righttoleft))