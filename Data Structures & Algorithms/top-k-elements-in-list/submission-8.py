class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])

        for num, freq in count.items():
            bucket[freq].append(num)
        
        for freq in range(len(bucket)-1, 0, -1):
            for num in bucket[freq]:
                answer.append(num)

                if len(answer) == k:
                    return answer