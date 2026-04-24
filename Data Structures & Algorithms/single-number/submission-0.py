class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        for num in frequency:
            if frequency[num] == 1:
                return num 