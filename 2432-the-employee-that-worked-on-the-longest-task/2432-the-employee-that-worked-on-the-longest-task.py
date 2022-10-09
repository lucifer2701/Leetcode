class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        li=[logs[0][1]]
        id=[]
        for i in range(len(logs)):
            id.append(logs[i][0])
        for i in range (1,len(logs)):
            li.append(logs[i][1]-logs[i-1][1])
        p=max(li)
        t=li.count(p)
        if t==1:
            x=li.index(p)
            return id[x]
        else:
            ans=[]
            for i in range(len(li)):
                if li[i]==p:
                    ans.append(logs[i][0])
            return min(ans)
            