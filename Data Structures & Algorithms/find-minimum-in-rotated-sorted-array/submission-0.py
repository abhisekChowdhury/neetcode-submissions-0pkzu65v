class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right, minNum = 0, len(nums)-1, nums[0]

        while left <= right:
            mid = (left + right) // 2
            currVal = nums[mid]

            minNum = min(minNum, currVal)

            if currVal <= nums[right]:
                if currVal >= minNum:
                    right = mid - 1
                else:
                    left = mid + 1
                    minNum = currVal
            else:
                if currVal >= minNum:
                    left = mid + 1
                else:
                    right = mid - 1
                    minNum = currVal
        return minNum
            
