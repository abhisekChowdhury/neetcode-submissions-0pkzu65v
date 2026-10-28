class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        left_max = 0
        right_max = 0
        units = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                units += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                units += right_max - height[right]
                right -= 1
        return units