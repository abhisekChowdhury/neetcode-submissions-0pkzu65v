class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create a frequency counter
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1

        heap = []
        heapq.heapify(heap)

        for value in freq.values():
            heapq.heappush(heap,-value)
        
        time = 0

        while heap:
            temp = []
            cycle = n+1

            for _ in range(cycle):
                if heap:
                    count = heapq.heappop(heap)
                    if count + 1 < 0:
                        temp.append(count + 1)
                time += 1

                if not heap and not temp:
                    break
            
            for item in temp:
                heapq.heappush(heap,item)
        return time