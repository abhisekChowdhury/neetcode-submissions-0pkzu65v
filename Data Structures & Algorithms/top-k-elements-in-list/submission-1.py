class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        count = defaultdict(int)

        for n in nums:
            count[n]+=1
        

        for i in range(len(nums) + 1):
            buckets.append([])
        
        for num in count:
            freq = count.get(num,0)
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                k-=1
                if k == 0:
                    return res