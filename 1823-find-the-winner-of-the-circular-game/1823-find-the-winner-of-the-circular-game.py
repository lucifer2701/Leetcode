class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        li=[i for i in range(1,n+1)]
        i=0
        while len(li)>1:
            j=i+k-1
            if j>=len(li):
                j=j%len(li)
            li.pop(j)
            i=j
        return li[0]