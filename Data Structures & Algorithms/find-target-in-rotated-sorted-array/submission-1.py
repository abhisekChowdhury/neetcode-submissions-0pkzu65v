class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            currentVal = nums[mid]

            if currentVal == target:
                return mid

            # Left half is sorted
            if nums[left] <= currentVal:
                if nums[left] <= target < currentVal:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if currentVal < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
