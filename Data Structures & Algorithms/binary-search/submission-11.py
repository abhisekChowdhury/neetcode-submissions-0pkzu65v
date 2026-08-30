class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        #[-1,0,2,4,6,8]
        # print(nums[(left + right) // 2])

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1

        return -1