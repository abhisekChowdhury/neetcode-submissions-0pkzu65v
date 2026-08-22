class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        heap = []

        for num in nums:
            count_map[num]+=1

        for num, freq in count_map.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq,num in heap]
        
        
