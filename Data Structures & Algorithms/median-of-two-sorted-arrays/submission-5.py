class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0.0

        if len(nums1) > len(nums2):
            nums1,nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)

        half = (m + n + 1)//2
        low = 0
        high = m

        while low <= high:
            i = (low + high) // 2
            j = half - i

            left1 = float('-inf')
            if i > 0:
                left1 = nums1[i-1]
            right1 = float('inf')
            if i<m:
                right1 = nums1[i]
            left2 = float('-inf')
            if j > 0:
                left2 = nums2[j-1]
            right2 = float('inf')
            if j < n:
                right2 = nums2[j]
            
            if left1 <= right2 and left2 <= right1:
                if (m+n)%2 == 1:
                    return float(max(left1,left2))
                return (max(left1,left2) + min(right1,right2)) / 2
            
            if left1 > right2:
                high = i - 1
            else:
                low = i + 1