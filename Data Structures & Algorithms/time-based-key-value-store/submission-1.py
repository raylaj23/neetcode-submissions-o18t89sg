class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = [(value, timestamp)]
        else:
            self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        v = self.timemap[key]
        
        res = ""
        st, dr = 0, len(v) - 1
        while st <= dr:
            mid = (st + dr) // 2
            val, time = v[mid][0], v[mid][1]

            if time <= timestamp:
                res = val
                st = mid + 1
            else:
                dr = mid - 1

        return res