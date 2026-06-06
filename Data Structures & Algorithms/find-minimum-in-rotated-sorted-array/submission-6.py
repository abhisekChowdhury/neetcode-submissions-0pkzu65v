class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        min_num = nums[0]

        while left <= right:
            mid = (left + right) // 2
            current_val = nums[mid]

            min_num = min(min_num, current_val)

            if current_val <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        
        return min_num