class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        #sort
        intervals.sort(key = lambda x: x[0])

        #initialize result
        result = [intervals[0]]

        #loop
        for start, end in intervals[1:]:
            last_end = result[-1][1]
            
            #merge or append
            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start,end])

        return result