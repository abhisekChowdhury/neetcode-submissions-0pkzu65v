class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for k in range(len(nums)):
                if i!=k:
                    if nums[i] == nums[k]:
                        return True

        return False