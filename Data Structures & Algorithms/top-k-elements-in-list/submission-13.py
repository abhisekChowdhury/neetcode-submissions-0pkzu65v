class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = defaultdict(int)

        for num in nums:
            count[num]+=1
        
        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        
        for num, frequency in count.items():
            bucket[frequency].append(num)
        
        for freq in range(len(bucket)-1,0,-1):
            for num in bucket[freq]:
                res.append(num)
            
                if len(res) == k:
                    return res
        
        return res