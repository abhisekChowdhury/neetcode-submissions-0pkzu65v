class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        # heapq.heapify(heap)
        
        for x,y in points:
            from_origin = x*x + y*y
            heapq.heappush(heap,(-from_origin, x,y))
            
            if len(heap) > k:
                heapq.heappop(heap)

        return [[x,y] for (dist,x,y) in heap]