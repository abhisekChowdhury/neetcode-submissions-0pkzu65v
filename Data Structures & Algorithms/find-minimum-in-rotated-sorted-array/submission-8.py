class Solution:
    def findMin(self, nums: List[int]) -> int:
        #easy brute force with time O(n) and space O(1)
        # return min(nums)
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left + right) // 2
            current = nums[mid]

            if current > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
