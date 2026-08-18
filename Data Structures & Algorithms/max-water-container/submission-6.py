class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #This is a two pointer question because I am considering two vairables. The height and the width.
        # [1,7,2,5,4,7,3,6]
        # the width will be the two pointers, left and right.
        # the height will be the min_value in heights

        left = 0
        right = len(heights)-1
        area = 0

        while left < right:
            width = right - left
            height = min(heights[left],heights[right])
            area = max(area, width * height)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return area