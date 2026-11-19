class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        left, right = 0, len(heights)-1

        while left < right:
            width = right - left
            height = min(heights[right],heights[left])
            vol = width * height

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
            max_vol = max(max_vol, vol)
        
        return max_vol