class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0

        for num in nums_set:
            count = 1
            while num + count in nums_set:
                count+=1
            max_count = max(count, max_count)

        return max_count