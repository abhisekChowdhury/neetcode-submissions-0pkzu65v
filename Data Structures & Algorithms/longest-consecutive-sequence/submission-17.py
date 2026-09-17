class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)
        max_count = 0
        for i in range(len(nums)):
            if nums[i]-1 not in visited:
                count = 1
                while count+nums[i] in visited:
                    count += 1
                max_count = max(max_count,count)
        return max_count
                    