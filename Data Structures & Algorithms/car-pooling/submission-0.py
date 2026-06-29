class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = {}

        for num_passengers, start, end in trips:
            changes[start] = changes.get(start,0) + num_passengers
            changes[end] = changes.get(end,0) - num_passengers
        
        total_passengers = 0

        for stop in sorted(changes):
            total_passengers += changes[stop]

            if total_passengers > capacity:
                return False
        
        return True