class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [] # needed to get the top k

        #count frequency of nums
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            while len(heap) > k:
                heapq.heappop(heap) 
        result = []
        for freq, num in heap:
            result.append(num)
        return result