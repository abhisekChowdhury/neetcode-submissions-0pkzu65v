class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num]+=1

        heap = []
        heapq.heapify(heap)
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq,num))

            while len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq,num in heap]
        


