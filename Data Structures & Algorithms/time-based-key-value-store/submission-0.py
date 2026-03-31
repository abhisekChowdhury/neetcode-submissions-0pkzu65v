class TimeMap:

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        
        value = ""

        # currentArr[] = storage[key]
        left = 0
        # right = len(currentArr[]) - 1
        right = len(self.storage[key]) - 1

        while left <= right:
            mid = (left + right) // 2
            currentTime = self.storage[key][mid][1]
            currentValue = self.storage[key][mid][0]

            if currentTime <= timestamp:
                value = currentValue
                left = mid + 1
            else:
                right = mid - 1

        return value 
