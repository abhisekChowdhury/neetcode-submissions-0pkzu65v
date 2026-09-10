class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        heap = [(freq,val) for val,freq in count.items()]
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        result = []
        for freq,value in heap:
            result.append(value)
        
        return result