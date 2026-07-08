class TimeMap:

    def __init__(self):
        self.items = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.items:
            self.items[key] = []
        self.items[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.items:
            return ""
        lists = self.items[key]
            
        l = 0
        r = len(lists)-1
        res = ""
        while l <= r:
            mid = (r-l)//2 + l
            if lists[mid][0] == timestamp:
                return lists[mid][1]
            elif lists[mid][0] < timestamp:
                l = mid+1
                res = lists[mid][1]
            else:
                r = mid-1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)