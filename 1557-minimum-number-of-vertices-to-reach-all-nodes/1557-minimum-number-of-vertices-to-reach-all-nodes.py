class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        li={};ans=[]
        for e in edges:
            li[e[1]]=1
        for i in range(n):
            if i not in li:
                ans.append(i)
        return ans
        