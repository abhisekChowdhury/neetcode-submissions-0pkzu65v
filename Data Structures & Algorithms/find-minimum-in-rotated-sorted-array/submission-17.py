class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        left_index = 0
        right_index = len(nums) - 1

        while left_index < right_index:
            middle_index = (left_index + right_index) // 2

            if nums[middle_index] > nums[right_index]:
                left_index = middle_index + 1
            
            else:
                right_index = middle_index
        
        return nums[left_index]