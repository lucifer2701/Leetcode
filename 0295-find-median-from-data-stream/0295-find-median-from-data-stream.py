from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.x=SortedList([])

    def addNum(self, num: int) -> None:
        self.x.add(num)
        

    def findMedian(self) -> float:
        if len(self.x)%2==1:
            return self.x[len(self.x)//2]
        else:
            return (self.x[len(self.x)//2]+self.x[(len(self.x)//2)-1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()