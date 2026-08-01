class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, path = [],[]

        def backtrack(index):
            if index == len(nums):
                result.append(path.copy())
                return
            
            backtrack(index + 1)
            path.append(nums[index])
            backtrack(index + 1)
            path.pop()
        
        backtrack(0)
        return result