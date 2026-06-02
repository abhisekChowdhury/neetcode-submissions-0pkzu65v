class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            current_num = nums[mid]

            if current_num == target:
                return mid
            elif current_num < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1