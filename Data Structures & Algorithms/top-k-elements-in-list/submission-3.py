class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first, we create a count dictionary to count how many times a number appeared
        count = defaultdict(int) # we use int since we are counting
        answer = []
        
        # this is how the counting happens of each number n
        for n in nums:
            count[n]+=1
        
        # create 0 - len(nums) buckets
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])
        
        # we will put each number in its frequency bucket
        # freq goes from 0 -> len(num)
        # each value goes in it's corresponding freq bucket
        # In case the nums are [7,7], here is what the following code will do:
        # {0 -> 0}
        # {1->[0]}
        # {2->[7, 7]}
        for num, freq in count.items():
            print('freq =', freq, 'num = ', num)
            bucket[freq].append(num)
        
        # we loop through the frequencies in the bucket from the end up until 0, since the last element is the highest frequency
        for freq in range(len(bucket) - 1, 0, -1):
            # check if there is num in bucket with that freq (for example, num = 7 and freq = 2)
            for num in bucket[freq]:
                # once that is found, append that to answer
                answer.append(num)
                # return answer when len(answer) == k
                if len(answer) == k:
                    return answer