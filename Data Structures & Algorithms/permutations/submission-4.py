class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, path = [],[]
        visited = [False] * len(nums)

        def backtrack(index):
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                path.append(nums[i])
                backtrack(index+1)
                path.pop()
                visited[i] = False
            
        backtrack(0)
        return result