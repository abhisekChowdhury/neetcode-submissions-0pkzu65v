class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left_index = 0
        right_index = len(height) - 1
        left_max = height[left_index]
        right_max = height[right_index]
        total_water = 0

        while left_index < right_index:
            if left_max < right_max:
                left_index += 1
                left_max = max(left_max, height[left_index])
                total_water += left_max - height[left_index]
            else:
                right_index -= 1
                right_max = max(right_max, height[right_index])
                total_water += right_max - height[right_index]

        return total_water