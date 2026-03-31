class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p1, p2 in points:
            dist = (p1*p1) + (p2*p2)
            heapq.heappush(heap, (dist, p1, p2))
        
        res = []
        for i in range(k):
            dist, p1, p2 = heapq.heappop(heap)
            res.append([p1,p2])
        
        return res
        
        