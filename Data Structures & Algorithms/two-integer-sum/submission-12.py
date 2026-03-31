class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dictionary = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dictionary:
                return [num_dictionary[complement], i]
            else:
                num_dictionary[num] = i
            
        return [0,0]
