class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # the median is either the middle value if odd number of values
        # or it is the average of the two middle values if even number of values

        nums = [0] * (len(nums1)+len(nums2))
        i = len(nums1) - 1
        k = len(nums2) - 1
        nums_counter = len(nums)-1

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
        
        left = 0; right = len(nums)-1
        mid = (left + right)//2

        #if even
        if len(nums) % 2 == 0:
            first = nums[mid]
            second = nums[mid+1]
            mid_number = (first + second) / 2
        #if odd
        else:
            mid_number = nums[mid]
    
        return mid_number