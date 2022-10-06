class TimeMap:

    def __init__(self):
        self.dic=defaultdict(deque)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].appendleft((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if self.dic[key]:
            for tv in self.dic[key]:	
                if tv[0] <= timestamp:
                    return tv[1]
        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)