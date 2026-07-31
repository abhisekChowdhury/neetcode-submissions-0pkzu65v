class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_count = 0
        count = 0
        for num in num_set:
            if num-1 not in num_set:
                count = 1
                while count + num in num_set:
                    count += 1
                
                max_count = max(count, max_count)
        
        return max_count