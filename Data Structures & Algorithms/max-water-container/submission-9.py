class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_width = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            current = width * height
            max_width = max(current, max_width)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_width