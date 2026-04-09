class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #sort from start
        intervals.sort(key = lambda x:x[0])

        #sort queries and keep original index
        queries = sorted((q,i) for i, q in enumerate(queries))

        #prepare result
        res = [-1] * len(queries)

        #min heap to store (interval_size, interval_end)
        heap = []

        #pointer for intervals
        i = 0

        for q, idx in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]

                #calculate size of interval
                size = end - start + 1

                #push to heap
                heapq.heappush(heap, (size,end))

                i+=1
            
            #remove intervals that end before q (invalid)
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            #now heap contains only intervals covering q
            if heap:
                res[idx] = heap[0][0] #smallest size
            else:
                res[idx] = -1
        
        return res