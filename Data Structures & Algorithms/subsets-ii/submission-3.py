class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, path = [],[]

        def backtrack(index):
            result.append(path.copy())

            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
            
            return result
        
        nums.sort()
        return backtrack(0)