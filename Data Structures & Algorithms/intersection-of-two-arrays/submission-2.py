class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        set2 = set(nums2)
        
        for num in nums1:
            if num in set2:
                res.add(num)
            continue
            
        return list(res)