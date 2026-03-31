class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        length = len(nums) - 1
        
        if len(nums) % 2 == 0:
            first = nums[length//2]
            second = nums[(length // 2) + 1]
            mid_num = (first + second) / 2
        else:
            mid_num = nums[length//2]

        return mid_num