class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = [0] * (len(nums1) + len(nums2))
        i = len(nums1) - 1
        k = len(nums2) - 1
        nums_counter = len(nums) - 1

        while i >= 0 and k >= 0:
            if nums1[i] > nums2[k]:
                nums[nums_counter] = nums1[i]
                i-=1
            else:
                nums[nums_counter] = nums2[k]
                k-=1
            nums_counter -= 1
        while i >= 0:
            nums[nums_counter] = nums1[i]
            nums_counter -= 1
            i -= 1
        while k >= 0:
            nums[nums_counter] = nums2[k]
            nums_counter -= 1
            k -= 1

        length = len(nums) - 1
        
        if len(nums) % 2 == 0:
            first = nums[length//2]
            second = nums[(length // 2) + 1]
            mid_num = (first + second) / 2
        else:
            mid_num = nums[length//2]

        return mid_num
            