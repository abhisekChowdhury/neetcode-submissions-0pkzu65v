class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        answer = []

        for n in nums:
            count[n]+=1
        
        bucket = []

        for i in range(len(nums) + 1):
            bucket.append([])
        
        for num, freq in count.items():
            bucket[freq].append(num)
        
        for freq in range(len(bucket)-1,0,-1):
            for num in bucket[freq]:
                answer.append(num)

                if k == len(answer):
                    return answer