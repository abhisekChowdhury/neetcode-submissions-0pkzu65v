class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0; right = len(nums)-1
        min_num = nums[0]
        while left < right:
            mid = (left + right) // 2

            # left is sorted
            current = nums[mid]

            if current > nums[right]:
                left += 1
            else:
                right = mid
        return nums[right]