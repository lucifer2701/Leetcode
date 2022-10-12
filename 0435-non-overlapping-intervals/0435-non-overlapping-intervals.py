class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        arr=intervals.copy()
        arr.sort(key=lambda x:x[1])
        print(arr)
        count=1
        prevS , prevE=arr[0]
        for s ,e in arr:
            if s<prevE:
                continue
            else:
                prevS , prevE = s , e
                count+=1
        return len(arr)-count