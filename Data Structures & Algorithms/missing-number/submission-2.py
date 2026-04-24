class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = [i for i in range(len(nums)+1)]
        print(expected)
        for e in expected:
            if e not in nums:
                return e