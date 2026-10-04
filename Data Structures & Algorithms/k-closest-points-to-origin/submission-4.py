class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        # heapq.heapify(heap)
        
        for x,y in points:
            from_origin = x*x + y*y
            heapq.heappush(heap,(from_origin, x,y))
        
        result = []
        for _ in range(k):
            distance, x,y = heapq.heappop(heap)
            result.append([x,y])

        return result