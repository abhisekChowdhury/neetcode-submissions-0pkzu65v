class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        
        # [1,7,2,5,4,7,3,6]

        # #1 and 7
        # vol = width * height
        # width = right pointer - left pointer
        # height = min(1,7)
        # vol = 1 * 1 = 1

        # Try for every combination - O(n^2)
        # Space - O(1)

        max_vol = 0
        left, right = 0, len(heights)-1
        while left < right:
            width = right-left
            height = min(heights[right],heights[left])
            vol = width * height

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            max_vol = max(max_vol, vol)

        return max_vol


