class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1]) #sort from end
        count = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            #overlap
            if start < prev_end:
                count+=1
            #no overlap
            else:
                prev_end = end
        
        return count
