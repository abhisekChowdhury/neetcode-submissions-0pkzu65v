class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2
            current_val = nums[mid]

            if current_val == target:
                return mid
            elif target < current_val:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
                
