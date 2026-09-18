class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find the unsorted part of the array

        left, right = 0, len(nums)-1

        while left < right:
            mid = (left + right) // 2
            current = nums[mid]
            #array is sorted
            if current <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[right]