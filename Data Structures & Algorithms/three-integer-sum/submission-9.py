class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            num1 = nums[i]
            target = -num1
            left = i + 1
            right = len(nums)-1

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.append([num1,nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        return result