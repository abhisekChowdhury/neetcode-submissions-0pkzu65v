class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in map:
                #return the index of 'difference' and current index i
                return [map[difference], i]
            else:
                #put the current num and current index i in map
                map[num] = i
        return []