class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result, path = [],[]
        visited = [False]*len(nums)

        def backtrack(index):
            if index == len(nums):
                result.append(path.copy())
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                
                visited[i] = True
                path.append(nums[i])
                backtrack(index+1)
                path.pop()
                visited[i] = False
            
        backtrack(0)
        return result