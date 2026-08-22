class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force
        #time - O(n^2)
        #space - O(1)

        # for i in range(len(nums)):
        #     for k in range(len(nums)):
        #         if i!=k:
        #             if nums[i] + nums[k] == target:
        #                 return [i,k]
                
        # return []

        #optimize time complexity with hashmap
        remaining = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in remaining:
                return [remaining[diff],i]
            else:
                remaining[nums[i]] = i
        return []
                