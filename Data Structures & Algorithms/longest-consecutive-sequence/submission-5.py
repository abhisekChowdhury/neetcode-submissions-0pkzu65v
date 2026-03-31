class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in num_set:
            length = 1

            # if num - 1 not in num_set:
            while num + 1 in num_set:
                length += 1
                num+=1
            
            longest = max(length, longest)
        
        return longest