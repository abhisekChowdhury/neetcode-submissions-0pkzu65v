class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        heap = [-c for c in freq.values()]
        heapq.heapify(heap)

        time = 0

        while heap:
            temp = []
            cycle = n+1

            for i in range(cycle):
                if heap:
                    count = heapq.heappop(heap)
                    if count + 1 < 0:
                        temp.append(count + 1)
                
                time += 1

                if not heap and not temp:
                    break
            
            for item in temp:
                heapq.heappush(heap, item)
        
        return time