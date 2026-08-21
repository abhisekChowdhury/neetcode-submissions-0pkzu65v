class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #brute force O(n)
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        #find the sorted array
        # [3,4,5,6,1,2]
        #find the mid, 5
        #if not greater than right, hence the left is sorted.
            # if target > left and target < mid:
                # right = mid - 1
            # else:
                # mid = left + 1
        # right is sorted.
            # if target > mid and target < right:
                # left = mid + 1
            # else:
                # mid = right - 1
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            current = nums[mid]

            if current == target:
                return mid
            elif nums[left] <= current:
                #left is sorted
                if target >= nums[left] and target < current:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                #right is sorted
                if target > current and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

