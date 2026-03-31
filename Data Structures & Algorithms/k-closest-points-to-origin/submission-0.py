class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # minheap of points based on their distance from the origin
        heap = []
        for p1,p2 in points:
            print("p1: ",p1, "p2: ",p2)

            distance = (p1*p1) + (p2*p2)
            heapq.heappush(heap, (distance, p1, p2))

        # return k minimum elements from the minheap
        res = []
        for i in range(k):
            # append the first k elements into a res 
            dist, p1, p2 = heapq.heappop(heap)
            res.append([p1,p2])

        return res