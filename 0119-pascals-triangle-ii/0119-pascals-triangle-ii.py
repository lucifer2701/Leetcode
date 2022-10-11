class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n=rowIndex
        li=[[1],[1,1]]
        if n==0:    return li[0]
        if n==1:    return li[1]
        li=[1,1]
        for i in range(2,n+1):
            li_=[1 for k in range(i+1)]
            for j in range(1,i):
                li_[j]=li[j-1]+li[j]
            li.clear()
            li=li_.copy()
        return li
            