class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        
        if len(nums1) < len(nums2):
            for num in nums1:
                if num in nums2:
                    res.add(num)
                continue
        else:
            for num in nums2:
                if num in nums1:
                    res.add(num)
                continue
            
        return list(res)