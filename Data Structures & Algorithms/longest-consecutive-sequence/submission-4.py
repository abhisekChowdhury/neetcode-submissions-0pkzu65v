class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for num in nums_set:
            
            length = 1

            if num-1 not in nums_set:
                while num+1 in nums_set:
                    length+=1
                    num+=1
            
            longest = max(longest, length)
        
        return longest