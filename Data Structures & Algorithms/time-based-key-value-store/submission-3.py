class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # for val,time in self.timemap[key]:
        #     print(val, time)

        if key not in self.storage:
            return ""
        
        current_array = self.storage[key]
        left = 0
        right = len(current_array) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2

            current_time = current_array[mid][1]
            current_value = current_array[mid][0]

            if current_time <= timestamp:
                result = current_value
                left = mid + 1
            else:
                right = mid - 1
        return result
