"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

#overlapping meetings require new rooms
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start) # sort by start time
        heap = []

        for interval in intervals:
            if heap and heap[0] <= interval.start:
                # remove min to merge
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
        
        return len(heap)
