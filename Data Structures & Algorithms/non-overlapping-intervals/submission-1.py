class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])

        prev_end = float("-inf") #target
        count = 0

        for start, end in intervals:
            if start >= prev_end:
                count+=1
                prev_end = end #update boundary
        
        return len(intervals) - count #represents number of overlaps