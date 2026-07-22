class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path, result = [],[]

        def backtrack(index):
            if index == len(nums):
                result.append(path[:])
                return
            
            #skip
            backtrack(index+1)

            #take
            path.append(nums[index])
            backtrack(index+1)
            path.pop()
        
        backtrack(0)

        return result