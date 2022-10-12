class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        li=intervals.copy()
        li.sort(key=lambda x:x[1])
        c=1
        prev0,prev1=li[0]
        for li0,li1 in li:
            if prev1>li0:   pass
            else:
                prev0,prev1=li0,li1
                c+=1
        return len(li)-c