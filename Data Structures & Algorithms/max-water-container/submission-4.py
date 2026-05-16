class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_amount = 0

        while left < right:
            current_amount = min(heights[left],heights[right])*(right - left)
            max_amount = max(current_amount, max_amount)

            if heights[right] > heights[left]:
                left+=1
            else:
                right-=1
        
        return max_amount